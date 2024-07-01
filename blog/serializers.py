from rest_framework import serializers
from .models import Tag, Blog, BlogComment, News, Gallery, Pastime
from services.slugify import unique_slug_generator
import pathlib
from services.decode import decodebase64_image
from services.check_model import get_or_none


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", )


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class BlogCreateSerializer(serializers.ModelSerializer):
    image_base64 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Blog
        fields = ("slug", "user", "image", "title", "content", "tags", "image_base64")
        extra_kwargs = {
            'user': {'read_only': True},
            'image': {'read_only': True},
        }

    def validate(self, attrs):
        image = attrs.get("image_base64", None)

        if image:
            if decodebase64_image(image) is None:
                raise serializers.ValidationError({'error': 'You can only upload image'})

        return attrs

    def create(self, validated_data):
        image_data = validated_data.pop("image_base64")
        tags = validated_data.pop("tags", [])

        blog = Blog.objects.create(**validated_data)

        for tag in tags:
            blog.tags.add(tag)

        if image_data:
            decode_image = decodebase64_image(image_data)
            blog.image = decode_image
            blog.save()

        return blog


class BlogUpdateSerializer(serializers.ModelSerializer):
    image_base64 = serializers.CharField(write_only=True)

    class Meta:
        model = Blog
        fields = ("slug", "user", "image", "title", "content", "tags", "image_base64")
        extra_kwargs = {
            'user': {'read_only': True},
            'image': {'read_only': True},
        }

    def validate(self, attrs):
        image = attrs.get("image_base64", None)

        if image:
            if decodebase64_image(image) is None:
                raise serializers.ValidationError({'error': 'You can only upload image'})

        return attrs

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image_base64')
        tags = validated_data.pop("tags", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.slug = unique_slug_generator(instance, slug_name=instance.title, old_slug=instance.slug,)
        instance.user = self.context.get('user')
        instance.save()

        if tags is not None:
            instance.tags.set(tags)

        if image_data:
            decode_image = decodebase64_image(image_data)
            instance.image = decode_image
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

