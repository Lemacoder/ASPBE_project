function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// Функция для отправки данных на сервер
function sendDataToServer(data) {
    fetch('/catalog/save_data/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Ошибка:', error));
}

// Отслеживаем наведение на элементы с классом .venue
let hoverTimer;
let startTime;
const hoverThreshold = 2000; // 2 секунды
const maxHoverTime = 10000; // 10 секунд

document.addEventListener('mouseover', function(event) {
    if (event.target.classList.contains('venue') || event.target.closest('.venue')) {
        const target = event.target.closest('.venue');
        if (target) {
            // Запоминаем время начала наведения
            startTime = Date.now();
        }
    }
});

// Отслеживаем уход курсора с элемента
document.addEventListener('mouseout', function(event) {
    if (event.target.classList.contains('venue') || event.target.closest('.venue')) {
        const target = event.target.closest('.venue');
        if (target) {
            const timeHovered = Date.now() - startTime;
            if (timeHovered >= hoverThreshold && timeHovered <= maxHoverTime) {
                const titleElement = document.querySelector('.venue__title');
                const title = titleElement.textContent;
                const result = {
                    venue_id: title,
                    action_type: 'Наведение'
                };
                sendDataToServer(result);
            }
        }
    }
});


document.addEventListener('click', function(event) {
    if (event.target.classList.contains('venue__link') || event.target.closest('.venue__link')) {
        const target = event.target.closest('.venue__link');
        if (target) {
            const titleElement = document.querySelector('.venue__title');
            const title = titleElement.textContent;
            const result = {
                venue_id: title,
                action_type: 'Нажатие'
            };
        
            sendDataToServer(result);
        }
    }
});


document.addEventListener('click', function(event) {
    if (event.target.classList.contains('place__info-button') || event.target.closest('.place__info-button')) {
        const target = event.target.closest('.place__info-button');
        if (target) {
            const titleElement = document.querySelector('.place__title');
            const title = titleElement.textContent;
            const result = {
                venue_id: title,
                action_type: 'Связаться'
            };
        
            sendDataToServer(result);
        }
    }
});

document.addEventListener('click', function(event) {
    if (event.target.classList.contains('place__like-button') || event.target.closest('.place__like-button')) {
        const target = event.target.closest('.place__like-button');
        if (target) {
            const titleElement = document.querySelector('.place__title');
            const title = titleElement.textContent;
            const result = {
                venue_id: title,
                action_type: 'Лайк'
            };
        
            sendDataToServer(result);
        }
    }
});




