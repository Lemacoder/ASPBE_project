from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    account_type = models.CharField(max_length=255, choices=[
        ('1', 'Пользователь'),
        ('2', 'Представитель')
    ])

    email_veryfy = models.BooleanField(default=False)

