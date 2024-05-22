from rest_framework import serializers
from .models import Blog, BlogComment
from services.slugify import unique_slug_generator


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


class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.slug = unique_slug_generator(instance, old_slug=self.context.get('slug'))
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
