from rest_framework import serializers
from .models import Blog, BlogComment, News, Gallery, Pastime
from services.slugify import unique_slug_generator
import pathlib


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
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


class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
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


class BlogDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", )


class BlogCommentListSerializer(serializers.ModelSerializer):
    blog = BlogListSerializer(read_only=True)

    class Meta:
        model = BlogComment
        fields = "__all__"


class BlogCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True}
        }


class BlogCommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True}
        }


class BlogCommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ("id", )


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
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


class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
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
        instance.save()

        return instance


class NewsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", )


class GalleryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class GalleryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"

    def validate(self, attrs):
        image = attrs.get("image", None)

        if image:
            file_path = pathlib.Path(str(image)).suffix

            if file_path not in ['.jpg', '.jpeg', '.png', '.heic']:
                raise serializers.ValidationError({'error': 'You can only share photos`'})

        return attrs


class GalleryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("id", )


class PastimeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastime
        fields = "__all__"


class PastimeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastime
        fields = "__all__"

    def validate(self, attrs):
        image = attrs.get("image", None)

        if image:
            file_path = pathlib.Path(str(image)).suffix

            if file_path not in ['.jpg', '.jpeg', '.png', '.heic']:
                raise serializers.ValidationError({'error': 'You can only share photos`'})

        return attrs


class PastimeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastime
        fields = "__all__"

    def validate(self, attrs):
        image = attrs.get("image", None)

        if image:
            file_path = pathlib.Path(str(image)).suffix

            if file_path not in ['.jpg', '.jpeg', '.png', '.heic']:
                raise serializers.ValidationError({'error': 'You can only share photos`'})

        return attrs


class PastimeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastime
        fields = ("id", )

