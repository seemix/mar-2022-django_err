from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.models import CarModel
from apps.cars.serializers import CarAllSerializer, CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset = queryset.order_by('brand', 'year')
        # queryset = queryset.reverse().order_by('brand', '-year')
        queryset = queryset.exclude(brand='bmw').order_by('brand', 'year')
        return queryset

    def get(self, *args, **kwargs):
        return super().list(*args, **kwargs)

    # def post(self, *args, **kwargs):
    #     return super().create(*args, **kwargs)


class CarRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
