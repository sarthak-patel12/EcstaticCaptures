# Generated by Django 5.0.2 on 2024-03-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_email_timer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_timer',
            name='time',
            field=models.TimeField(),
        ),
    ]
