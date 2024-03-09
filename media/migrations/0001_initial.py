# Generated by Django 5.0.2 on 2024-02-26 14:49

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
            name='Image',
            fields=[
                ('image', models.ImageField(upload_to='images/')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['subuser'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('video', models.FileField(upload_to='videos/')),
                ('subuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['subuser'],
            },
        ),
    ]
