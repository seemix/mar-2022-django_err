from rest_framework.serializers import ModelSerializer

from apps.cars.models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year', 'engine', 'price')


class CarAllSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'year')
