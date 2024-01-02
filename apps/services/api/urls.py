from django.urls import path

from apps.services.api.api import (
    LashServiceCreateApiView,
    ReserveServiceApiView,
    LashServiceDeleteUpdateViewSet
)

urlpatterns = [
    path('service/', LashServiceCreateApiView.as_view(), name='service'),
    path('delete-update-service/<int:pk>/',
         LashServiceDeleteUpdateViewSet.as_view(
             {'delete': 'destroy',
              'put': 'update',
              'patch': 'partial_update',
              }
         ),
         name='delete-update-service'),
    path('reserve/', ReserveServiceApiView.as_view(), name='service'),
]
