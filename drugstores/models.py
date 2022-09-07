from django.db import models


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

    def schedule_representation(self):
        try:
            return f'Время открытия в понедельник - {self.schedule.monday_open}'
        except Exception:
            return 'Расписания нет'

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








