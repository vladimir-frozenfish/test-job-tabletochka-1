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


