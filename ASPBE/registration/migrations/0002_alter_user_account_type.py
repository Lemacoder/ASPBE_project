# Generated by Django 5.1.4 on 2025-03-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('1', 'Пользователь'), ('2', 'Представитель')], max_length=255),
        ),
    ]
