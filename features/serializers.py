from rest_framework import serializers
import pathlib
from django.contrib.auth import get_user_model
from services.check_model import get_or_none
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
        fields = ("file", "id")

    def validate(self, attrs):
        file = attrs.get("file", None)

        if file:
            file_path = pathlib.Path(str(file)).suffix

            if file_path not in ['.mkv', '.mp4', '.mov', '.jpg', '.jpeg', '.png', '.gif', '.heic']:
                raise serializers.ValidationError({'error': 'You can only share photos and videos'})

        return attrs


class StoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ("status", )


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
        fields = ("story", "comment", )


class StoryCommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryComment
        fields = ("comment", )


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
        fields = ("story", )

    def create(self, validated_data):
        story, created = StoryLike.objects.get_or_create(**validated_data)

        if not created:
            story.delete()

        return story


# Story Comment Like

class StoryCommentLikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryCommentLike
        fields = ("id", "story_comment", "user")


class StoryCommentLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryCommentLike
        fields = ("story_comment", )

    def create(self, validated_data):
        story_comment, created = StoryCommentLike.objects.get_or_create(**validated_data)

        if not created:
            story_comment.delete()

        return story_comment
