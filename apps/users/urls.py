from django.urls import path

from .views import AddAvatarView, UserCreateView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/avatar', AddAvatarView.as_view())
]
