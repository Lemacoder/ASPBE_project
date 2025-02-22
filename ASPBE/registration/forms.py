from django import forms
from UserMainMenu.models import Users


class AddUser(forms.ModelForm):
    name = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    login = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    account_type = forms.MultipleChoiceField(choices=((1, 'Личный'), (2, 'Представитель')), widget=forms.RadioSelect)
    auntificatiuon = forms.BooleanField()

    class Meta:
        model = Users
        fields = '__all__'



"""
<form>
                
                <p><label for="f.is_for_label">{{ f.label }}</label>{{ f }}</p>
                <input type="text" placeholder="ФИО" required>
                
                <label>Введите логин</label>
                <input type="email" placeholder="Почта" required>
                
                <label>Введите пароль*</label>
                <input type="password" placeholder="Пароль" required>
                <small>Пароль должен содержать минимум 8 символов, a-z, A-Z, 0-9, |@#$%^&*</small>
                
                <label>Повторите пароль</label>
                <input type="password" placeholder="Повторите пароль" required>
                
                <a href=""><button type="submit">&#10132;</button></a>
            </form>
            """





