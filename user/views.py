from rest_framework import generics
from .serializers import (
    LoginSerializer, RegisterSerializer, ResetPasswordSerializer, ResetPasswordCheckSerializer,
    ResetPasswordCompleteSerializer, ChangePasswordSerializer, ProfileSerializer
)
from django.contrib.auth import get_user_model
from django.utils.encoding import smart_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.permissions import IsAuthenticated
from .models import Profile

User = get_user_model()


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ResetPasswordView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer


class ResetPasswordCheckView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordCheckSerializer
    lookup_field = "uuid"

    def get_object(self):
        # convert uuid to id and get user
        uuid = self.kwargs.get(self.lookup_field)
        id_ = smart_str(urlsafe_base64_decode(uuid))
        return User.objects.get(id=int(id_))


class ResetPasswordCompleteView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordCompleteSerializer
    lookup_field = "uuid"

    def get_object(self):
        # convert uuid to id and get user
        uuid = self.kwargs.get(self.lookup_field)
        id_ = smart_str(urlsafe_base64_decode(uuid))
        return User.objects.get(id=int(id_))


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = IsAuthenticated,

    def get_object(self):
        return self.request.user


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile





