from rest_framework import serializers

from drugstores.models import Drugstore


class DrugstoreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'drugstore_id',
            'phone'
        )
        model = Drugstore