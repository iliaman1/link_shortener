# Generated by Django 5.0.2 on 2024-02-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('full_url', models.URLField(unique=True, verbose_name='Полная ссылка')),
                ('short_url', models.CharField(db_index=True, unique=True, verbose_name='Сокращенная ссылка')),
            ],
            options={
                'ordering': ('-updated_at',),
            },
        ),
    ]