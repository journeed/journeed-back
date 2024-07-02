from rest_framework import generics
from .models import Country, City
from .serializers import CountryListSerializer, CityListSerializer


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer





