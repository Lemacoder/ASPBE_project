# Generated by Django 5.1.4 on 2025-02-07 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HoldingMainMenu', '0003_emploees_holding'),
        ('UserMainMenu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emploees',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserMainMenu.users'),
        ),
        migrations.AddField(
            model_name='emploees',
            name='holding_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HoldingMainMenu.holding'),
        ),
    ]
