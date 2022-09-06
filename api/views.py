from rest_framework import viewsets

from drugstores.models import Drugstore

from .serializers import DrugstoreSerializer


class DrugstoreViewSet(viewsets.ModelViewSet):
    queryset = Drugstore.objects.all()
    serializer_class = DrugstoreSerializer

