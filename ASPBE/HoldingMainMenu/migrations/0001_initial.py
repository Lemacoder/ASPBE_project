# Generated by Django 5.2 on 2025-05-06 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VenueTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Emploees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooles', models.IntegerField()),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('holding_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HoldingMainMenu.holding')),
            ],
        ),
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('square', models.IntegerField()),
                ('wardrobe', models.BooleanField()),
                ('parking', models.BooleanField()),
                ('status', models.IntegerField(default=0, editable=False)),
                ('embedding', models.TextField(blank=True, null=True)),
                ('holding_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HoldingMainMenu.holding')),
                ('venue_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HoldingMainMenu.venuetags')),
            ],
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HoldingMainMenu.venues')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='holdings/')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HoldingMainMenu.venues')),
            ],
        ),
        migrations.CreateModel(
            name='VenueService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.TextField()),
                ('venue_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HoldingMainMenu.venuetags')),
            ],
        ),
    ]
