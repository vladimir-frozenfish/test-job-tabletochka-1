from django.db import models


class Drugstore(models.Model):
    drugstore_id = models.CharField(
        max_length=75, primary_key=True, verbose_name='Идентификатор аптеки'
    )
    phone = models.CharField(
        max_length=20, verbose_name='Телефон'
    )

    class Meta:
        verbose_name_plural = 'Аптеки'
        verbose_name = 'Аптека'
        ordering = ['drugstore_id']

    def __str__(self):
        return self.drugstore_id