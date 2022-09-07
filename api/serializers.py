from rest_framework import serializers

from drugstores.models import (Drugstore,
                               Schedule)
from .utils import format_time


class ScheduleSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format='%H:%M')

    class Meta:
        fields = (
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
        model = Schedule

    def to_representation(self, instance):
        return [
            {
                'day': 1,
                'day_name': 'Пн',
                'start': format_time(instance.monday_open),
                'end': format_time(instance.monday_close)
            },
            {
                'day': 2,
                'day_name': 'Вт',
                'start': format_time(instance.tuesday_open),
                'end': format_time(instance.tuesday_close)
            },
            {
                'day': 3,
                'day_name': 'Ср',
                'start': format_time(instance.wednesday_open),
                'end': format_time(instance.wednesday_close)
            },
            {
                'day': 4,
                'day_name': 'Чт',
                'start': format_time(instance.thursday_open),
                'end': format_time(instance.thursday_close)
            },
            {
                'day': 5,
                'day_name': 'Пт',
                'start': format_time(instance.friday_open),
                'end': format_time(instance.friday_close)
            },
            {
                'day': 6,
                'day_name': 'Сб',
                'start': format_time(instance.saturday_open),
                'end': format_time(instance.saturday_close)
            },
            {
                'day': 7,
                'day_name': 'Вс',
                'start': format_time(instance.sunday_open),
                'end': format_time(instance.sunday_close)
            },
        ]


class DrugstoreSerializer(serializers.ModelSerializer):

    schedule = ScheduleSerializer()

    class Meta:
        fields = (
            'created_at',
            'updated_at',
            'drugstore_id',
            'phone',
            'schedule_representation',
            'schedule'
        )
        model = Drugstore


class DrugstoreCreateSerializer(serializers.ModelSerializer):
    """сериализатор для создания записи об аптеке"""

    class Meta:
        fields = (
            'drugstore_id',
            'phone'
        )
        model = Drugstore

    def to_representation(self, instance):
        return {
            'drugstore_id': instance.drugstore_id
        }
