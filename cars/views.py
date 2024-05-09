from .models import Car, CarImage, CarCategory, Steering, Fuel
from rest_framework import generics
from services.pagination import CarListPagination
from django.db.models import F, FloatField
from django.db.models.functions import Coalesce
from .serializers import (
    CarListSerializer, CarDetailSerializer, CarCategorySerializer, SteeringSerializer,
    FuelSerializer, CarCreateSerializer, CarImageSerializer
)
from rest_framework.permissions import IsAuthenticated
from services.permissions import CarsPermission
from rest_framework.response import Response


class CarCategoryListView(generics.ListAPIView):
    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer


class SteeringListView(generics.ListAPIView):
    queryset = Steering.objects.all()
    serializer_class = SteeringSerializer


class FuelListView(generics.ListAPIView):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer


class CarListView(generics.ListAPIView):
    queryset = Car.objects.annotate(
        disc_prc=Coalesce(F("discount_price"), 0, output_field=FloatField()),
        total_price=F("price")-F("disc_prc")
    )
    serializer_class = CarListSerializer
    pagination_class = CarListPagination


class MyCarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    pagination_class = CarListPagination
    permission_classes = (
        IsAuthenticated,
        CarsPermission
    )

    def get_queryset(self):
        return Car.objects.annotate(
        disc_prc=Coalesce(F("discount_price"), 0, output_field=FloatField()),
        total_price=F("price") - F("disc_prc")).filter(user=self.request.user)


class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.annotate(
        disc_prc=Coalesce(F("discount_price"), 0, output_field=FloatField()),
        total_price=F("price") - F("disc_prc")
    ).all()
    serializer_class = CarDetailSerializer
    lookup_field = "id"


class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer
    permission_classes = (IsAuthenticated, CarsPermission)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"data": request.data})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data)


class CarEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarCreateSerializer
    permission_classes = (IsAuthenticated, CarsPermission)
    lookup_field = "id"

    def get_queryset(self):
        return Car.objects.annotate(
        disc_prc=Coalesce(F("discount_price"), 0, output_field=FloatField()),
        total_price=F("price") - F("disc_prc")).filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            instance=self.get_object(),
            context={"data": request.data}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data)


class CarImageDeleteView(generics.DestroyAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = (IsAuthenticated, CarsPermission)

