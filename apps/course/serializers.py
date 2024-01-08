from rest_framework import serializers

from apps.course.models import CourseType, Course, CourseReservation
from apps.users.serializers import ProfileSerializer


class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = '__all__'

    def create(self, validated_data):
        return CourseType.objects.create(**validated_data)


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

