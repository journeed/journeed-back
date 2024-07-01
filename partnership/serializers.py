from rest_framework import serializers
import re
from .models import *


class ApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipApplication
        fields = "__all__"


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipApplication
        fields = ("company_name", "industry", "partnership_method", "currency", "message", )

    def validate(self, attrs):
        company_name = attrs.get('company_name')

        filter_company_name = r'^[a-zA-Z0-9 -]{1,50}$'

        if not re.match(filter_company_name, company_name.lower()):
            raise serializers.ValidationError({'error': 'Please write your company name correctly'})

        return attrs


class ApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipApplication
        fields = ("id", "is_confirm")


class ApplicationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipApplication
        fields = ("id", )
