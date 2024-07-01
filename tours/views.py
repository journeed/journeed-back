from django.shortcuts import render
from .models import Tour, TourReview
from rest_framework import generics
from .serializers import TourListSerializer, TourReviewListSerializer


class TourListView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourListSerializer


class TourDetailView(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourListSerializer
    lookup_field = "slug"


class TourReviewListView(generics.ListAPIView):
    queryset = TourReview.objects.all()
    serializer_class = TourReviewListSerializer


