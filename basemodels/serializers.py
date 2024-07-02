from rest_framework import serializers
from .models import Country, City


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


