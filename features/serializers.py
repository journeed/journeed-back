from rest_framework import serializers
import pathlib
from django.contrib.auth import get_user_model
from services.check_model import get_or_none
from services.validate_file import validate_photo_and_video
from .models import Story, StoryComment, StoryLike, StoryCommentLike

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
        fields = ("id", "user", "status", "file")
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def validate(self, attrs):
        file = attrs.get("file", None)

        if validate_photo_and_video(file) is False:
            raise serializers.ValidationError({'error': 'You can only share photos and videos'})

        return attrs


class StoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ("id", "user", "status", )
        extra_kwargs = {
            'user': {'read_only': True},
        }


class StoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        story_like = instance.storylike_set.all()
        repr_['like_count'] = story_like.count()

        return repr_


# Story Comment

class StoryCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = "__all__"

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        story_comment_like = instance.storycommentlike_set.all()
        repr_['like_count'] = story_comment_like.count()

        return repr_


class StoryCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = ("id", "user", "story", "comment", )
        extra_kwargs = {
            'user': {'read_only': True},
        }


class StoryCommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = ("id", "user", "comment", )
        extra_kwargs = {
            'user': {'read_only': True},
        }


class StoryCommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = ("id", )


# Story Like

class StoryLikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryLike
        fields = ("id", "story", "user")


class StoryLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryLike
        fields = ("id", "story", "user")
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def create(self, validated_data):
        story, created = StoryLike.objects.get_or_create(**validated_data)

        return story


class StoryLikeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryLike
        fields = ("id", )


# Story Comment Like

class StoryCommentLikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryCommentLike
        fields = ("id", "story_comment", "user")


class StoryCommentLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryCommentLike
        fields = ("id", "story_comment", "user")
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def create(self, validated_data):
        story_comment, created = StoryCommentLike.objects.get_or_create(**validated_data)

        return story_comment


class StoryCommentLikeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryCommentLike
        fields = ("id", )
