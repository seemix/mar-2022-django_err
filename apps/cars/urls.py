from django.urls import path

from apps.cars.views import AttachPhotoCarView, CarListCreateView, CarRetrieveUpdateDestroy

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroy.as_view()),
    path('/<int:pk>/photo', AttachPhotoCarView.as_view())
]
