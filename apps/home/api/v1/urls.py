from django.urls import path

from apps.home.api.v1.api import HomeApiView

urlpatterns = [
    path('home/', HomeApiView(), name='home')
]
