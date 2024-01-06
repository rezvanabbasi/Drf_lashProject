from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.course.models import Course, CourseReservation
from apps.course.serializers import CourseTypeSerializer, CourseSerializer, CourseReservationSerializer
from apps.users.models import Profile
from config.permissions import IsTeacherPermission, IsLearnerPermission


class CourseTypeApiView(APIView):
    permission_classes = (IsAuthenticated, IsTeacherPermission)

    def post(self, request):
        serializer = CourseTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CourseApiView(APIView):
    permission_classes = (IsAuthenticated, IsTeacherPermission)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        teacher = Profile.objects.get(user_id=request.user.id)
        course = Course(
            title=request.data['title'],
            teacher_id=teacher.id,
            course_capacity=request.data['course_capacity'],
            course_sessions=request.data['course_sessions'],
            course_start_date=request.data['course_start_date'],
            course_duration=request.data['course_duration'],
            comment=request.data['comment']
        )
        course.save()

        return Response(data={"Create Course"}, status=status.HTTP_200_OK)

    def get(self):
        queryset = Course.objects.all()
        serializer = CourseSerializer(data=queryset, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CourseReservationApiView(APIView):
    permission_classes = (IsAuthenticated, IsLearnerPermission)

    def post(self, request):
        serializer = CourseReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile = Profile.objects.get(user_id=request.user.id)
        reserve = CourseReservation(
            student_id=profile.id,
            course_id=request.data['course_id']
        )
        reserve.save()
        return Response(data={"You reserve this course"}, status=status.HTTP_200_OK)

    def get(self):
        """
        return all courses  reserved by this user who authenticated.
        """
        pass
