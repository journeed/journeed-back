from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Story, StoryComment
from .serializers import (StoryListSerializer, StoryCreateSerializer, StoryDetailSerializer,
                          StoryCommentListSerializer, StoryCommentCreateSerializer, StoryCommentUpdateSerializer,
                          StoryCommentDeleteSerializer
                          )
from .permission import AccessPermission, StoryPermission, StoryCommentPermission


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
    permission_classes = [StoryPermission]
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
    permission_classes = (IsAuthenticated, StoryCommentPermission)
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class StoryCommentDeleteView(generics.DestroyAPIView):
    queryset = StoryComment.objects.all()
    serializer_class = StoryCommentDeleteSerializer
    permission_classes = (IsAuthenticated, StoryCommentPermission)
    lookup_field = "id"
