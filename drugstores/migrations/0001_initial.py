# Generated by Django 4.1.1 on 2022-09-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugstore',
            fields=[
                ('drugstore_id', models.CharField(max_length=75, primary_key=True, serialize=False, verbose_name='Идентификатор аптеки')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Аптека',
                'verbose_name_plural': 'Аптеки',
                'ordering': ['drugstore_id'],
            },
        ),
    ]
