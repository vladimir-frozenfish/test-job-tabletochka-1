# Generated by Django 4.1.1 on 2022-09-08 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drugstores', '0005_city_geo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='geo',
            options={'ordering': ['drugstore'], 'verbose_name': 'Местоположение аптеки', 'verbose_name_plural': 'Местоположения аптек'},
        ),
        migrations.RemoveField(
            model_name='drugstore',
            name='region',
        ),
    ]