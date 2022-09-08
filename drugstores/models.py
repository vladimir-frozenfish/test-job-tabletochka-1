import uuid
from django.db import models

from .utils import get_schedule_representation


class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(
        max_length=100, verbose_name='Регион'
    )

    class Meta:
        verbose_name_plural = 'Регионы'
        verbose_name = 'Регион'
        ordering = ['name']

    def __str__(self):
        return self.name


class Drugstore(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата изменения'
    )
    drugstore_id = models.CharField(
        max_length=75, primary_key=True, verbose_name='Идентификатор аптеки'
    )
    phone = models.CharField(
        max_length=20, verbose_name='Телефон'
    )
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE,
        related_name='drugstore', verbose_name='Регион аптеки',
        blank=True, null=True
    )

    def schedule_representation(self):
        try:
            return get_schedule_representation(self)
        except Exception:
            return 'Расписания нет'

    schedule_representation.short_description = 'Время работы аптеки'

    class Meta:
        verbose_name_plural = 'Аптеки'
        verbose_name = 'Аптека'
        ordering = ['drugstore_id']

    def __str__(self):
        return self.drugstore_id


class Schedule(models.Model):
    drugstore = models.OneToOneField(
        Drugstore, on_delete=models.CASCADE,
        related_name='schedule', verbose_name='Аптека'
    )
    monday_open = models.TimeField(blank=True, null=True, verbose_name='Понедельник открытие')
    monday_close = models.TimeField(verbose_name='Понедельник закрытие')
    tuesday_open = models.TimeField(blank=True, null=True, verbose_name='Вторник открытие')
    tuesday_close = models.TimeField(verbose_name='Вторник закрытие')
    wednesday_open = models.TimeField(blank=True, null=True, verbose_name='Среда открытие')
    wednesday_close = models.TimeField(verbose_name='Среда закрытие')
    thursday_open = models.TimeField(blank=True, null=True, verbose_name='Четверг открытие')
    thursday_close = models.TimeField(verbose_name='Четверг закрытие')
    friday_open = models.TimeField(blank=True, null=True, verbose_name='Пятница открытие')
    friday_close = models.TimeField(verbose_name='Пятница закрытие')
    saturday_open = models.TimeField(blank=True, null=True, verbose_name='Суббота открытие')
    saturday_close = models.TimeField(verbose_name='Суббота закрытие')
    sunday_open = models.TimeField(blank=True, null=True, verbose_name='Воскресенье открытие')
    sunday_close = models.TimeField(verbose_name='Воскресенье закрытие')

    class Meta:
        verbose_name_plural = 'Расписание аптек'
        verbose_name = 'Расписание аптеки'
        ordering = ['drugstore']

    def __str__(self):
        return self.drugstore.drugstore_id








