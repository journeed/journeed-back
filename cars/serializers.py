from rest_framework import serializers
from .models import Car, CarImage, CarCategory, Steering, CarReview, Fuel


class CarImageSerializer(serializers.ModelSerializer):
    car_image_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CarImage
        fields = (
            "car_image_id",
            "image"
        )

    def get_car_image_id(self, obj):
        return obj.id


class CarCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CarCategory
        fields = (
            "id",
            "name"
        )


class SteeringSerializer(serializers.ModelSerializer):

    class Meta:
        model = Steering
        fields = (
            "id",
            "name",
        )


class FuelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fuel
        fields = (
            "id",
            "name"
        )


class CarReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarReview
        fields = (
            "id",
            "car",
            "user",
            "content",
            "rating"
        )
        extra_kwargs = {
            "car": {"write_only": True},
            "user": {"write_only": True}
        }


class CarReviewEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarReview
        fields = (
            "content",
            "rating"
        )


class CarListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)
    total_price = serializers.FloatField(read_only=True)
    steering = SteeringSerializer(read_only=True)
    type_car = CarCategorySerializer(read_only=True)

    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "image",
            "type_car",
            "steering",
            "person_count",
            "price",
            "total_price",
        )

    def get_image(self, obj):
        image = obj.carimage_set.first()
        return CarImageSerializer(image).data


class CarDetailSerializer(serializers.ModelSerializer):
    total_price = serializers.FloatField(read_only=True)
    steering = SteeringSerializer(read_only=True)
    type_car = CarCategorySerializer(read_only=True)
    fuel = FuelSerializer(read_only=True)

    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "description",
            "type_car",
            "steering",
            "person_count",
            "fuel",
            "price",
            "total_price",
        )

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        images_qs = instance.carimage_set.all()
        images = CarImageSerializer(images_qs, many=True).data
        repr_["images"] = images

        review_qs = instance.carreview_set.all()
        repr_["review"] = {
            "review_count": review_qs.count(),
            "reviews": CarReviewSerializer(review_qs, many=True).data
        }
        return repr_


class CarCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            "name",
            "description",
            "type_car",
            "steering",
            "fuel",
            "fuel_volume",
            "person_count",
            "price",
            "discount_price"
        )

    def create(self, validated_data):
        images = self.context.get("data").getlist("images")
        new_car = Car.objects.create(**validated_data)
        for image in images:
            CarImage.objects.create(
                car=new_car, image=image
            )
        return new_car

    def update(self, instance, validated_data):
        instance.carimage_set.all().delete()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        images = self.context.get("data").getlist("images")  # request'ten resimleri al
        for image in images:
            CarImage.objects.create(car=instance, image=image)

        return instance

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        images = instance.carimage_set.all()
        repr_["images"] = CarImageSerializer(images, many=True).data
        return repr_

