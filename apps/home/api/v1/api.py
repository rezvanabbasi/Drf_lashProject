from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.course.models import Course
from apps.home.serializers import HomeSerializer
from apps.services.models import LashService


class HomePageApiView(APIView):
    """
    Display all services and all courser for this department.
    """
    def get(self, *args, **kwargs):
        services = LashService.objects.all()
        course = Course.objects.all()

        data = {
            "services": services,
            "course": course
        }

        serializer = HomeSerializer(data)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
