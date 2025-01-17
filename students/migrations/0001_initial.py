# Generated by Django 5.1.4 on 2025-01-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='students-images/')),
                ('group', models.ManyToManyField(blank=True, related_name='student_groups', to='groups.group')),
            ],
        ),
    ]
