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
        return f'{self.phone} - {self.updated_at}'

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
    monday_open = models.CharField(max_length=5, blank=True, verbose_name='Понедельник открытие')
    monday_close = models.CharField(max_length=5, verbose_name='Понедельник закрытие')
    tuesday_open = models.CharField(max_length=5, blank=True, verbose_name='Вторник открытие')
    tuesday_close = models.CharField(max_length=5, verbose_name='Вторник закрытие')
    wednesday_open = models.CharField(max_length=5, blank=True, verbose_name='Среда открытие')
    wednesday_close = models.CharField(max_length=5, verbose_name='Среда закрытие')
    thursday_open = models.CharField(max_length=5, blank=True, verbose_name='Четверг открытие')
    thursday_close = models.CharField(max_length=5, verbose_name='Четверг закрытие')
    friday_open = models.CharField(max_length=5, blank=True, verbose_name='Пятница открытие')
    friday_close = models.CharField(max_length=5, verbose_name='Пятница закрытие')
    saturday_open = models.CharField(max_length=5, blank=True, verbose_name='Суббота открытие')
    saturday_close = models.CharField(max_length=5, verbose_name='Суббота закрытие')
    sunday_open = models.CharField(max_length=5, blank=True, verbose_name='Воскресенье открытие')
    sunday_close = models.CharField(max_length=5, verbose_name='Воскресенье закрытие')

    class Meta:
        verbose_name_plural = 'Расписание аптек'
        verbose_name = 'Расписание аптеки'
        ordering = ['drugstore']

    def __str__(self):
        return self.drugstore.drugstore_id








