from rest_framework import serializers
from .models import Tour, TourReview


class TourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"


class TourReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourReview
        fields = "__all__"



