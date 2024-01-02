from rest_framework import serializers
from apps.services.models import LashService, ReserveService
from apps.users.serializers import ProfileSerializer
from apps.users.models import Profile


class LashServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LashService
        fields = '__all__'


class LashServiceDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LashService
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.material = validated_data.get('material', instance.material)
        instance.price = validated_data.get('price', instance.price)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.staff = self.context['staff']
        instance.save()
        return instance


class ReserveServiceSerializer(serializers.ModelSerializer):
    service = LashServiceSerializer()
    customer = ProfileSerializer()

    class Meta:
        model = ReserveService
        fields = '__all__'

    def create(self, validated_data):
        reserve = ReserveService(
            comment=validated_data["comment"]
        )
        customer = validated_data["customer"]
        service = validated_data["service"]

        reserve.customer = customer
        reserve.service = service

        service.is_available = False
        service.save()

        reserve.save()

        return reserve
