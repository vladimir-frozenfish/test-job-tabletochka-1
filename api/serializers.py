from rest_framework import serializers

from drugstores.models import Drugstore


class DrugstoreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'created_at',
            'updated_at',
            'drugstore_id',
            'phone',
            'schedule_representation'
        )
        model = Drugstore


class DrugstoreCreateSerializer(serializers.ModelSerializer):

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
