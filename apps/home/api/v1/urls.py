from django.urls import path

from apps.home.api.v1.api import HomePageApiView

urlpatterns = [
    path('home-page/', HomePageApiView.as_view(), name='home-page')
]
