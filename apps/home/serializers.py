from rest_framework import serializers

from apps.course.models import Course
from apps.services.models import LashService


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LashServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LashService
        fields = '__all__'


class HomeSerializer(serializers.Serializer):
    services = LashServiceSerializer(many=True)
    course = CourseSerializer(many=True)
