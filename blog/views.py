from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Blog, BlogComment, Advice
from .serializers import *
from services.permission import ManagerPermission, ObjectPermission


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    lookup_field = "slug"


class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer
    permission_classes = (ManagerPermission, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogUpdateSerializer
    permission_classes = (ManagerPermission, )
    lookup_field = "slug"

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, instance=self.get_object(),
                                           context={"user": self.request.user,
                                                    "slug": self.kwargs.get("slug")})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)


class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDeleteSerializer
    permission_classes = (ManagerPermission, )
    lookup_field = "slug"


class BlogCommentListView(generics.ListAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentListSerializer

    def get_queryset(self):
        BlogComment.objects


class BlogCommentCreateView(generics.CreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentCreateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class BlogCommentUpdateView(generics.UpdateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentUpdateSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class BlogCommentDeleteView(generics.DestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentDeleteSerializer
    permission_classes = (IsAuthenticated, ObjectPermission)
    lookup_field = "id"


class AdviceListView(generics.ListAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceListSerializer


class AdviceDetailView(generics.RetrieveAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceListSerializer
    lookup_field = "slug"


class AdviceCreateView(generics.CreateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceCreateSerializer
    permission_classes = (ManagerPermission, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class AdviceUpdateView(generics.UpdateAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceUpdateSerializer
    permission_classes = (ManagerPermission, )
    lookup_field = "slug"

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class AdviceDeleteView(generics.DestroyAPIView):
    queryset = Advice.objects.all()
    serializer_class = AdviceDeleteSerializer
    permission_classes = (ManagerPermission, )
    lookup_field = "slug"


class GalleryListView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryListSerializer


class GalleryCreateView(generics.CreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryCreateSerializer
    permission_classes = (ManagerPermission, )

    def perform_create(self, serializer):
        return serializer.save()


class GalleryDeleteView(generics.DestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryDeleteSerializer
    permission_classes = (ManagerPermission, )
    lookup_field = "id"


class PastimeListView(generics.ListAPIView):
    queryset = Pastime.objects.all()
    serializer_class = PastimeListSerializer


class PastimeCreateView(generics.CreateAPIView):
    queryset = Pastime.objects.all()
    serializer_class = PastimeCreateSerializer
    permission_classes = (ManagerPermission, )

    def perform_create(self, serializer):
        return serializer.save()


class PastimeUpdateView(generics.UpdateAPIView):
    queryset = Pastime.objects.all()
    serializer_class = PastimeUpdateSerializer
    permission_classes = (ManagerPermission, )
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save()


class PastimeDeleteView(generics.DestroyAPIView):
    queryset = Pastime.objects.all()
    serializer_class = PastimeDeleteSerializer
    permission_classes = (ManagerPermission, )
    lookup_field = "id"

