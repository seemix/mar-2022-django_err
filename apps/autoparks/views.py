from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AutoParkSerializer
from .models import AutoParkModel


# Create your views here.
from ..cars.serializers import CarSerializer


class AutoParksListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = CarSerializer

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        car = self.request.data
        serializer = self.get_serializer(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        return Response(serializer.data, status.HTTP_201_CREATED)


