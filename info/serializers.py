from rest_framework import serializers
import re
from .models import AboutInfo, DifferentInfo, SocialMedia, ContactInfo, Contact


class AboutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInfo
        fields = "__all__"


class DifferentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifferentInfo
        fields = "__all__"


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("name", "email", "phone", "request_type", "message", )

    def validate(self, attrs):
        name = attrs.get('name')

        filter_name = r'^[a-zA-Z]{1,15}$'
        # name verification
        if not re.match(filter_name, name.lower()):
            raise serializers.ValidationError({'error': 'Please write your first name correctly'})

        return attrs
