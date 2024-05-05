from rest_framework import serializers
import pathlib
from django.contrib.auth import get_user_model
from services.check_model import get_or_none
from .models import Story, StoryComment

Users = get_user_model()


# Story


class StoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class StoryCreateSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Story
        fields = ("file", "id")

    def validate(self, attrs):
        file = attrs.get("file", None)

        if file:
            file_path = pathlib.Path(str(file)).suffix

            if file_path not in ['.mkv', '.mp4', '.mov', '.jpg', '.jpeg', '.png', '.gif', '.heic']:
                raise serializers.ValidationError({'error': 'You can only share photos and videos'})

        return attrs


class StoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


# Story Comment


class StoryCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = "__all__"


class StoryCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = ("story", "comment", )


class StoryCommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = ("comment", )


class StoryCommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = ("id", )

