from rest_framework import viewsets, status
from rest_framework.response import Response

from drugstores.models import City, Geo, Region, Drugstore, Schedule

from .serializers import (DrugstoreSerializer,
                          DrugstoreCreateSerializer,
                          ScheduleSerializer,
                          GeoSerializer)
from .utils import format_schedule


class DrugstoreViewSet(viewsets.ModelViewSet):
    queryset = Drugstore.objects.all()
    serializer_class = DrugstoreSerializer

    def update(self, request, *args, **kwargs):
        """редактирование записи об аптеке"""

        instance = self.get_object()

        """получение нового расписания, валидация его"""
        data_schedule = format_schedule(request.data.get('schedule'))
        schedule_serializer = ScheduleSerializer(data=data_schedule)
        schedule_serializer.is_valid(raise_exception=True)

        """geo, получение или создание нового города и соответственно региона"""
        geo = request.data.get('geo')
        if geo is None:
            return Response(
                {'message': 'Необходимо указать местоположение аптеки'},
                status=status.HTTP_400_BAD_REQUEST
            )

        region, create_region = Region.objects.get_or_create(id=geo['region_id'], name=geo['region_name'])
        city, create_city = City.objects.get_or_create(id=geo['city_id'], name=geo['city_name'], region=region)
        geo['location_lat'] = geo['location']['lat']
        geo['location_lon'] = geo['location']['lon']
        geo_serializer = GeoSerializer(data=geo)
        geo_serializer.is_valid(raise_exception=True)

        """сохранение основной информации о аптеке"""
        instance.drugstore_id = request.data.get('drugstore_id', instance.drugstore_id)
        instance.phone = request.data.get('phone', instance.phone)
        instance.save()

        """удаление старого расписания и сохранение нового расписания"""
        Schedule.objects.filter(drugstore=instance).delete()
        drugstore = Drugstore.objects.get(drugstore_id=instance.drugstore_id)
        schedule_serializer.save(drugstore=drugstore)

        """удаление старого местоположения и сохранение нового местоположения"""
        Geo.objects.filter(drugstore=instance).delete()
        geo_serializer.save(city=city, drugstore=drugstore)

        instance_serializer = DrugstoreSerializer(instance)

        return Response(instance_serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        """создание записи об аптеке"""

        """получение данных о расписании"""
        if 'schedule' in request.data:
            schedule = request.data.pop('schedule')
        else:
            return Response(
                {'message': 'Необходимо указать расписание аптеки'},
                status=status.HTTP_400_BAD_REQUEST
            )

        """получение данных о месторасположении аптеки"""
        if 'geo' in request.data:
            geo = request.data.pop('geo')
        else:
            return Response(
                {'message': 'Необходимо указать месторасположение аптеки'},
                status=status.HTTP_400_BAD_REQUEST
            )

        """geo, получение или создание нового города и соответственно региона"""
        region, create_region = Region.objects.get_or_create(id=geo['region_id'], name=geo['region_name'])
        city, create_city = City.objects.get_or_create(id=geo['city_id'], name=geo['city_name'], region=region)
        geo['location_lat'] = geo['location']['lat']
        geo['location_lon'] = geo['location']['lon']
        geo_serializer = GeoSerializer(data=geo)
        geo_serializer.is_valid(raise_exception=True)

        """преобразование данных о расписание для модели и сериализатора,
        валидация данных о расписании"""
        data_schedule = format_schedule(schedule)
        schedule_serializer = ScheduleSerializer(data=data_schedule)
        schedule_serializer.is_valid(raise_exception=True)

        """валидация основных данных аптеки, сохранение записи аптеки,
        сохранение записи о расписании аптеки, сохранение записи о 
        местоположении аптеки"""
        drugstore_serializer = DrugstoreCreateSerializer(data=request.data)
        drugstore_serializer.is_valid(raise_exception=True)
        drugstore = drugstore_serializer.save()
        schedule_serializer.save(drugstore=drugstore)
        geo_serializer.save(city=city, drugstore=drugstore)

        return Response(
            {'drugstore_id': drugstore_serializer.data['drugstore_id']},
            status=status.HTTP_201_CREATED
        )
