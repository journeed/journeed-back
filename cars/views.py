from .models import (
    Car, CarImage, CarCategory, Steering, Fuel, CarReview
)
from rest_framework import generics
from services.pagination import CarListPagination
from django.db.models import F, FloatField, Avg, IntegerField
from django.db.models.functions import Coalesce
from .serializers import (
    CarListSerializer, CarDetailSerializer, CarCategorySerializer, SteeringSerializer,
    FuelSerializer, CarCreateSerializer, CarImageSerializer, CarReviewSerializer,
    CarReviewEditSerializer
)
from rest_framework.permissions import IsAuthenticated
from services.permission import CarsPermission, CarReviewPermission
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


class AnnotatedCarQuerysetMixin:
    def get_queryset(self):
        queryset = Car.objects.annotate(
            disc_prc=Coalesce(F("discount_price"), 0, output_field=FloatField()),
            total_price=F("price") - F("disc_prc"),
            rating=Coalesce(Avg("carreview__rating"), 0, output_field=IntegerField())
        )
        return queryset


class CarListView(AnnotatedCarQuerysetMixin, generics.ListAPIView):
    serializer_class = CarListSerializer
    pagination_class = CarListPagination


class TrendCarsView(AnnotatedCarQuerysetMixin, generics.ListAPIView):
    serializer_class = CarListSerializer
    pagination_class = CarListPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-rating", "-view_count")[:6]


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

    def get(self, request, *args, **kwargs):
        car = self.get_object()
        car.view_count += 1
        car.save()

        return super().get(request, *args, **kwargs)


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


class CarReviewCreateView(generics.CreateAPIView):
    queryset = CarReview.objects.all()
    serializer_class = CarReviewSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CarReviewEditView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarReviewEditSerializer
    permission_classes = (IsAuthenticated, CarReviewPermission)
    lookup_field = "id"

    def get_queryset(self):
        return CarReview.objects.filter(user=self.request.user)


