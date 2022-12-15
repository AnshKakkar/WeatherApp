from rest_framework import serializers

from .models import Preference

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Preference
        fields='__all__'
