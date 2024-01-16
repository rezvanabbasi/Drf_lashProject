from rest_framework import serializers

from apps.course.models import CourseType, Course, CourseReservation
from apps.users.serializers import ProfileSerializer


class CourseTypeSerializer(serializers.ModelSerializer):
    """
    Serialize date from course.api.CourseTypeApiView.
    """

    class Meta:
        model = CourseType
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    teacher = ProfileSerializer

    class Meta:
        model = Course
        fields = '__all__'


class CourseReservationSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    student = ProfileSerializer()

    class Meta:
        model = CourseReservation
        fields = '__all__'
