from rest_framework.viewsets import ModelViewSet

from core.models import Carro
from core.serializers import CarroSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer