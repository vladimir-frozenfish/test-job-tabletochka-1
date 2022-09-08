from rest_framework import viewsets, status
from rest_framework.response import Response

from drugstores.models import Drugstore, Schedule

from .serializers import (DrugstoreSerializer,
                          DrugstoreCreateSerializer,
                          ScheduleSerializer)
from .utils import format_schedule


class DrugstoreViewSet(viewsets.ModelViewSet):
    queryset = Drugstore.objects.all()
    serializer_class = DrugstoreSerializer

    def update(self, request, *args, **kwargs):
        """редактирование записи об аптеке"""

        instance = self.get_object()

        """получение нового расписания, удаление старного раписания"""
        data_schedule = format_schedule(request.data.get('schedule'))
        Schedule.objects.filter(drugstore=instance).delete()

        """сохранение основной информации о аптеке"""
        instance.drugstore_id = request.data.get('drugstore_id', instance.drugstore_id)
        instance.phone = request.data.get('phone', instance.phone)
        instance.save()

        """сохранение нового расписания"""
        drugstore = Drugstore.objects.get(drugstore_id=instance.drugstore_id)
        Schedule.objects.create(drugstore=drugstore, **data_schedule)

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

        """преобразование данных о расписание для модели и сериализатора,
        валидация данных о расписании"""
        data_schedule = format_schedule(schedule)
        schedule_serializer = ScheduleSerializer(data=data_schedule)
        schedule_serializer.is_valid(raise_exception=True)

        """валилация основных данных аптеки, сохранение записи аптеки,
        сохранение записи о расписании аптеки"""
        drugstore_serializer = DrugstoreCreateSerializer(data=request.data)
        drugstore_serializer.is_valid(raise_exception=True)
        drugstore = drugstore_serializer.save()
        Schedule.objects.create(drugstore=drugstore, **data_schedule)

        return Response(
            {'drugstore_id': drugstore_serializer.data['drugstore_id']},
            status=status.HTTP_201_CREATED
        )
