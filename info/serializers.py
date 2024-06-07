from rest_framework import serializers
import re
import pathlib
from .models import *
from services.validate import validate_photo


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


