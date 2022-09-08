from rest_framework import serializers

from drugstores.models import (
    Drugstore,
    Region,
    Schedule
)
from .utils import format_time, format_schedule


class ScheduleSerializer(serializers.ModelSerializer):

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
        read_only_fields = ('drugstore',)

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

    # def to_internal_value(self, data):
    #     return data


class RegionSerializer(serializers.ModelSerializer):
    region_id = serializers.CharField(source='id')
    region_name = serializers.CharField(source='name')

    class Meta:
        fields = (
            'region_id',
            'region_name'
        )
        model = Region


class DrugstoreSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(required=False)
    geo = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'created_at',
            'updated_at',
            'drugstore_id',
            'geo',
            'phone',
            'schedule_representation',
            'schedule'
        )
        model = Drugstore

    def get_geo(self, obj):
        region = RegionSerializer(obj.region)
        return region.data

    '''
    def update(self, instance, data):
        """редактирование записи о аптеке"""

        """получение нового расписания, удаление старного раписания"""
        data_schedule = format_schedule(data.get('schedule'))
        Schedule.objects.filter(drugstore=instance).delete()

        """сохранение основной информации о аптеке"""
        instance.drugstore_id = data.get('drugstore_id', instance.drugstore_id)
        instance.phone = data.get('phone', instance.phone)
        instance.save()

        """сохранение нового расписания"""
        drugstore = Drugstore.objects.get(drugstore_id=instance.drugstore_id)
        Schedule.objects.create(drugstore=drugstore, **data_schedule)

        return instance
    '''


class GeoSerializer(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data


class DrugstoreCreateSerializer(serializers.ModelSerializer):
    """сериализатор для создания записи об аптеке"""
    # schedule = ScheduleSerializer(required=True)
    # geo = GeoSerializer(required=True)

    class Meta:
        fields = (
            'drugstore_id',
            # 'geo',
            'phone',
            # 'schedule'
        )
        model = Drugstore

    '''
    def to_representation(self, instance):
        return {
            'drugstore_id': instance.drugstore_id
        }
    '''

    '''
    def create(self, data):
        print(data)
        try:
            schedule = data.pop('schedule')
        except:
            raise serializers.ValidationError(
                {'message': 'Необходимо указать время работы аптеки'}
            )

        """создание записи аптеки, получение правильного формата для раписания,
        создания записи расписания для вновь созданно аптеки"""
        data_schedule = format_schedule(schedule)
        drugstore = Drugstore.objects.create(**data)
        Schedule.objects.create(drugstore=drugstore, **data_schedule)

        return drugstore
    '''
