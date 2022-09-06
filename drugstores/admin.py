from django.contrib import admin

from .models import Drugstore


class DrugstoreAdmin(admin.ModelAdmin):
    list_display = (
        'drugstore_id',
        'phone'
    )
    list_display_links = ('drugstore_id', )


admin.site.register(Drugstore, DrugstoreAdmin)


