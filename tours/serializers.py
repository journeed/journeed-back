from rest_framework import serializers
from .models import Tour, TourReview
from services.validate_file import validate_photo
from services.slugify import unique_slug_generator
from partnership.models import TourOrganizer


class TourListSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tour
        fields = "__all__"
        extra_kwargs = {
            "rating": {"read_only": True}
        }


class TourCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "city": {"required": True}
        }

    def validate(self, attrs):
        image = attrs.get("image", None)

        if image:
            if validate_photo(image) is False:
                return serializers.ValidationError({"error": "You can share only photo"})

        return attrs


class TourUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True}
        }

    def validate(self, attrs):
        image = attrs.get("image", None)

        if image:
            if validate_photo(image) is False:
                return serializers.ValidationError({"error": "You can share only photo"})

        return attrs

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.slug = unique_slug_generator(instance,
                                              slug_name=f'{instance.city.country.name}-{instance.city.name}',
                                              old_slug=instance.slug)

        organizer_user = TourOrganizer.objects.get(partnership__user=self.context.get("user"))
        instance.user = organizer_user
        instance.save()

        return instance


class TourDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "slug"


# Tour review

class TourReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourReview
        fields = "__all__"


class TourReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourReview
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "rating": {"required": True},
        }


class TourReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourReview
        fields = "__all__"
        extra_kwargs = {
            "tour": {"read_only": True},
            "user": {"read_only": True},
        }


class TourReviewDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourReview
        fields = "__all__"


