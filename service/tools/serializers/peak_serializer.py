from rest_framework import serializers

from service.models import Mountain


class PeakSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mountain
        fields = (
            'id',
            'name',
            'longitude',
            'latitude',
            'altitude',
        )
