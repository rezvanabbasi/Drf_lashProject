from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from apps.services.models import LashService, ReserveService
from config.permissions import IsAdminOrStaffPermission
from apps.services.serializerz import (
    LashServiceSerializer,
    ReserveServiceSerializer,
    LashServiceDeleteUpdateSerializer
)

from apps.users.models import Profile


class LashServiceCreateApiView(APIView):
    """
    Create lash service by manager.
    """
    permission_classes = [IsAuthenticated, IsAdminOrStaffPermission]

    def post(self, request):
        serializer = LashServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile = Profile.objects.get(user_id=request.user.id)
        service = LashService(
            title=request.data['title'],
            material=request.data['material'],
            price=request.data['price'],
            duration=request.data['duration'],
            staff=profile
        )
        service.save()
        return Response(status=status.HTTP_201_CREATED)


class LashServiceDeleteUpdateViewSet(viewsets.ModelViewSet):
    """
    Delete and update lash service for both of
     authenticated and admin user.
    When use 'delete' http method do destroy,
    When use 'put' http method do update.
    """
    serializer_class = LashServiceDeleteUpdateSerializer
    queryset = LashService.objects.all()
    permission_classes = (IsAuthenticated, IsAdminOrStaffPermission)
    http_method_names = ['delete', 'put']

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        # you custom logic #
        return super(LashServiceDeleteUpdateViewSet, self).destroy(request, pk, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        instance = self.get_object()
        data = {
            "title": request.data['title'],
            # "image": request.data['image'],
            "material": request.data['material'],
            "price": request.data['price'],
            "duration": request.data['duration'],
        }
        serializer = self.serializer_class(instance=instance,
                                           data=data,  # or request.data
                                           context={'staff': profile},
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReserveServiceApiView(APIView):
    """
    By use post http method reserve a lash service,

    By use get http method show all of service reservation.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReserveServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        serializer = ReserveServiceSerializer(
            data=ReserveService.objects.all(),
            many=True
        )
        serializer.is_valid(raise_exception=False)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK)
