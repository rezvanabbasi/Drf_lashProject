from django.urls import path

from apps.home.api.api import HomeApiView

urlpatterns = [
    path('home/', HomeApiView(), name='home')
]
