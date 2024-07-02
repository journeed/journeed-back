from django.db.models import Avg, IntegerField
from django.db.models.functions import Coalesce
from .models import Tour, TourReview
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from services.permission import ToursPermission, ObjectPermission
from partnership.models import TourOrganizer


class TourListView(generics.ListAPIView):
    serializer_class = TourListSerializer

    def get_queryset(self):
        return Tour.objects.annotate(rating=Coalesce(Avg("tourreview__rating"), 0, output_field=IntegerField()))


class TourDetailView(generics.RetrieveAPIView):
    serializer_class = TourListSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Tour.objects.annotate(rating=Coalesce(Avg("tourreview__rating"), 0, output_field=IntegerField()))


class TourCreateView(generics.CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourCreateSerializer
    permission_classes = (ToursPermission, )

    def perform_create(self, serializer):
        organizer_user = TourOrganizer.objects.get(partnership__user=self.request.user)
        return serializer.save(user=organizer_user)


class TourUpdateView(generics.UpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourUpdateSerializer
    permission_classes = (ToursPermission, )
    lookup_field = "slug"

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, instance=self.get_object(),
                                           context={"user": self.request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, instance=self.get_object(),
                                           context={"user": self.request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)


class TourDeleteView(generics.DestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourUpdateSerializer
    permission_classes = (ToursPermission, )
    lookup_field = "slug"


class TourReviewListView(generics.ListAPIView):
    queryset = TourReview.objects.all()
    serializer_class = TourReviewListSerializer


class TourReviewCreateView(generics.CreateAPIView):
    queryset = TourReview.objects.all()
    serializer_class = TourReviewCreateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class TourReviewUpdateView(generics.UpdateAPIView):
    queryset = TourReview.objects.all()
    serializer_class = TourReviewUpdateSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class TourReviewDeleteView(generics.DestroyAPIView):
    queryset = TourReview.objects.all()
    serializer_class = TourReviewDeleteSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "id"

