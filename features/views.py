from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Story, StoryComment, StoryLike, StoryCommentLike
from .serializers import *
from services.permission import ManagerPermission, ObjectPermission


# Story

class StoryListView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSerializer

    def get_queryset(self):
        return Story.objects.filter(status="Activated")


class StoryCreateView(generics.CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class StoryUpdateView(generics.UpdateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryUpdateSerializer
    permission_classes = [ManagerPermission]
    lookup_field = "id"


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
    serializer_class = StoryDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return Story.objects.filter(status="Activated")


# Story Comment

class StoryCommentListView(generics.ListAPIView):
    serializer_class = StoryCommentListSerializer
    lookup_field = "story"

    def get_queryset(self):
        return StoryComment.objects.filter(story=self.kwargs.get("story"))


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
    serializer_class = StoryLikeListSerializer
    lookup_field = "story"

    def get_queryset(self):
        return StoryLike.objects.filter(story=self.kwargs.get("story"))


class StoryLikeCreateView(generics.CreateAPIView):
    queryset = StoryLike.objects.all()
    serializer_class = StoryLikeCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class StoryLikeDeleteView(generics.DestroyAPIView):
    queryset = StoryLike.objects.all()
    serializer_class = StoryLikeDeleteSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "story"


# Story Comment Like

class StoryCommentLikeListView(generics.ListAPIView):
    serializer_class = StoryCommentLikeListSerializer
    lookup_field = "story_comment"

    def get_queryset(self):
        return StoryCommentLike.objects.filter(story_comment=self.kwargs.get("story_comment"))


class StoryCommentLikeCreateView(generics.CreateAPIView):
    queryset = StoryCommentLike.objects.all()
    serializer_class = StoryCommentLikeCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class StoryCommentLikeDeleteView(generics.DestroyAPIView):
    queryset = StoryCommentLike.objects.all()
    serializer_class = StoryCommentLikeCreateSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "id"


