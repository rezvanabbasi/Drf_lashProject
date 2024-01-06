from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status

from apps.course.models import Course
from apps.course.serializers import CourseTypeSerializer, CourseSerializer
from config.settings.permissions import IsTeacherPermission


class CourseTypeApiView(APIView):
    permission_classes = (IsAuthenticated, IsTeacherPermission)

    def post(self, request):
        serializer = CourseTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsTeacherPermission)
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=request.data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'Invalid data!'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self):
        queryset = self.queryset
        serializer = self.serializer_class(data=queryset, many=True)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={'Access Denied!'}, status=status.HTTP_403_FORBIDDEN)
