# Generated by Django 5.1.3 on 2024-12-27 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('experience', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='teachers_images/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='subjects.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
