from django.contrib import admin

from .models import (
    City,
    Drugstore,
    Geo,
    Region,
    Schedule
)


class DrugstoreAdmin(admin.ModelAdmin):
    list_display = (
        'drugstore_id',
        'geo',
        # 'region',
        'created_at',
        'updated_at',
        'phone',
        'schedule_representation'
    )
    list_display_links = ('drugstore_id', )
    readonly_fields = ('schedule_representation', )


class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        'drugstore',
        'monday_open',
        'monday_close',
        'tuesday_open',
        'tuesday_close',
        'wednesday_open',
        'wednesday_close',
        'thursday_open',
        'thursday_close',
        'friday_open',
        'friday_close',
        'saturday_open',
        'saturday_close',
        'sunday_open',
        'sunday_close'
    )


class RegionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = ('id', 'name')


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'region'
    )
    list_display_links = ('id', 'name')


class GeoAdmin(admin.ModelAdmin):
    list_display = (
        'drugstore',
        'address',
        'city',
        'location_lat',
        'location_lon'
    )


admin.site.register(Drugstore, DrugstoreAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Geo, GeoAdmin)



