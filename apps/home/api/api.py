from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.course.models import Course
from apps.home.serializers import HomeSerializer
from apps.services.models import LashService


class HomeApiView(APIView):
    def get(self):
        services = LashService.objects.all()
        course = Course.objects.all()

        data = {
            "services": services,
            "course": course
        }

        serializer = HomeSerializer(data)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
