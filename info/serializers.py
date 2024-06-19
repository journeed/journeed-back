from rest_framework import serializers
import re
import pathlib
from .models import *
from services.validate import validate_photo
from services.slugify import unique_slug_generator


# Home Page Info

class HomeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeInfo
        fields = "__all__"


class HomeInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeInfo
        fields = ("head", "first_content", "second_content", "home_background",
                  "home_banner", "home_banner_background")

        @staticmethod
        def validate_photo(photo):
            if photo:
                photo_path = pathlib.Path(str(photo)).suffix
                allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.heic']

                return photo_path in allowed_extensions
            pass

        def validate(self, attrs):
            home_background = attrs.get("home_background", None)
            home_banner_background = attrs.get("home_banner_background", None)

            if home_background or home_banner_background:
                if self.validate_photo(home_background) is False or self.validate_photo(home_background) is False:
                    return serializers.ValidationError({"error": "You can only upload photos"})

            return attrs


class HomeInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeInfo
        fields = ("head", "first_content", "second_content", "home_background",
                  "home_banner", "home_banner_background")

    def validate(self, attrs):
        home_background = attrs.get("home_background", None)
        home_banner_background = attrs.get("home_banner_background", None)

        if home_background or home_banner_background:
            if validate_photo(home_background) is False or validate_photo(home_background) is False:
                return serializers.ValidationError({"error": "You can only upload photos"})
            
        return attrs


class HomeInfoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeInfo
        fields = ("id", )


class SpecialOfferListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = "__all__"


class SpecialOfferCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def validate(self, attrs):
        image = attrs.get("image", None)

        if image:
            file_path = pathlib.Path(str(image)).suffix

            if file_path not in ['.jpg', '.jpeg', '.png', '.heic']:
                raise serializers.ValidationError({'error': 'You can only share photos`'})

        return attrs


class SpecialOfferUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def validate(self, attrs):
        image = attrs.get("image", None)

        if image:
            file_path = pathlib.Path(str(image)).suffix

            if file_path not in ['.jpg', '.jpeg', '.png', '.heic']:
                raise serializers.ValidationError({'error': 'You can only share photos`'})

        return attrs

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.slug = unique_slug_generator(instance, old_slug=instance.slug)
        instance.user = self.context.get('user')
        instance.save()

        return instance


class SpecialOfferDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = ("id", )


# About Page Info

class AboutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInfo
        fields = "__all__"


class AboutInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInfo
        fields = ("slogan", "head", "background", "first_content", "second_content")

    def validate(self, attrs):
        background = attrs.get("background")

        if validate_photo(background) is False:
            return serializers.ValidationError({"error": "You can only upload photos"})

        return attrs


class AboutInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInfo
        fields = ("slogan", "head", "background", "first_content", "second_content")

    def validate(self, attrs):
        background = attrs.get("background")

        if validate_photo(background) is False:
            return serializers.ValidationError({"error": "You can only upload photos"})

        return attrs


class AboutInfoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInfo
        fields = ("id", )


class DifferentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifferentInfo
        fields = "__all__"


class DifferentInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifferentInfo
        fields = ("head", "content")


class DifferentInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifferentInfo
        fields = ("head", "content")


class DifferentInfoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifferentInfo
        fields = ("id", )


# Social Media Info

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"


class SocialMediaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("name", "url")


class SocialMediaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("name", "url")


class SocialMediaDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("id", )


# Contact Page Info

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class ContactInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ("mobile", "mail", "work_time", "social_media", "map")


class ContactInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ("mobile", "mail", "work_time", "social_media", "map")


class ContactInfoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ("id", )


# Contact

class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("name", "email", "phone", "request_type", "message", )

    def validate(self, attrs):
        name = attrs.get('name')

        filter_name = r'^[a-zA-Z]{1,15}$'
        # name verification
        if not re.match(filter_name, name.lower()):
            raise serializers.ValidationError({'error': 'Please write your name correctly'})

        return attrs


class ContactDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("id", )


# Partnership Page Info

class PartnershipFeatureInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipFeatureInfo
        fields = "__all__"


class PartnershipFeatureInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipFeatureInfo
        fields = ("title", "text")


class PartnershipFeatureInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipFeatureInfo
        fields = ("title", "text")


class PartnershipFeatureInfoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipFeatureInfo
        fields = ("id", )


class PartnershipTypeInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipTypeInfo
        fields = "__all__"


class PartnershipTypeInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipTypeInfo
        fields = ("title", "international", "domestic", "image")


class PartnershipTypeInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipTypeInfo
        fields = ("title", "international", "domestic", "image")


class PartnershipTypeInfoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipTypeInfo
        fields = ("id", )


class PartnershipCommissionInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipCommissionInfo
        fields = "__all__"


class PartnershipCommissionInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipCommissionInfo
        fields = ("title", "text")


class PartnershipCommissionInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipCommissionInfo
        fields = ("title", "text")


class PartnershipCommissionInfoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipCommissionInfo
        fields = ("id", )


class PartnershipFaqInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipFaqInfo
        fields = "__all__"


class PartnershipFaqInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipFaqInfo
        fields = ("title", "text")


class PartnershipFaqInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipFaqInfo
        fields = ("title", "text")


class PartnershipFaqInfoDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipFaqInfo
        fields = ("id", )



