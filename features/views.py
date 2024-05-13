from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Story, StoryComment, StoryLike, StoryCommentLike
from .serializers import *
from services.permission import AccessPermission, OtherPermission, ObjectPermission


# Story

class StoryListView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSerializer


class StoryCreateView(generics.CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateSerializer
    permission_classes = [AccessPermission]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class StoryDetailView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        story = self.get_object()
        story.view_count += 1
        story.save()

        data = {"story_id": story.id}

        return Response(data, status=200)


class StoryDeleteView(generics.DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer
    permission_classes = [OtherPermission]
    lookup_field = "id"


# Story Comment

class StoryCommentListView(generics.ListAPIView):
    queryset = StoryComment.objects.all()
    serializer_class = StoryCommentListSerializer


class StoryCommentCreateView(generics.CreateAPIView):
    queryset = StoryComment.objects.all()
    serializer_class = StoryCommentCreateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class StoryCommentUpdateView(generics.UpdateAPIView):
    queryset = StoryComment.objects.all()
    serializer_class = StoryCommentUpdateSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class StoryCommentDeleteView(generics.DestroyAPIView):
    queryset = StoryComment.objects.all()
    serializer_class = StoryCommentDeleteSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "id"


# Story like

class StoryLikeListView(generics.ListAPIView):
    queryset = StoryLike.objects.all()
    serializer_class = StoryLikeListSerializer


class StoryLikeCreateView(generics.CreateAPIView):
    queryset = StoryLike.objects.all()
    serializer_class = StoryLikeCreateSerializer
    permission_classes = (OtherPermission,)

    # def post(self, request, *args, **kwargs):
    #     story_id = request.data.get("story")
    #     story, created = StoryLike.objects.get_or_create(story_id=story_id, user=request.user)
    #
    #     if not created:
    #         story.delete()
    #
    #     serializer = self.serializer_class(story).data
    #
    #     return Response(serializer, status=200)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


# Story Comment Like

class StoryCommentLikeListView(generics.ListAPIView):
    queryset = StoryCommentLike.objects.all()
    serializer_class = StoryCommentLikeListSerializer


class StoryCommentLikeCreateView(generics.CreateAPIView):
    queryset = StoryCommentLike.objects.all()
    serializer_class = StoryCommentLikeCreateSerializer
    permission_classes = (OtherPermission,)

    # def post(self, request, *args, **kwargs):
    #     story_comment_id = request.data.get("story_comment")
    #     story_comment, created = StoryCommentLike.objects.get_or_create(story_comment_id=story_comment_id, user=request.user)
    #
    #     if not created:
    #         story_comment.delete()
    #
    #     serializer = self.serializer_class(story_comment).data
    #
    #     return Response(serializer, status=200)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


