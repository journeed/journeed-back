from rest_framework import generics
from .models import HomeInfo, AboutInfo, DifferentInfo, SocialMedia, ContactInfo, Contact
from .serializers import *
from services.permission import ManagerPermission, ManagerObjectPermission
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail


class HomeInfoView(generics.RetrieveAPIView):
    queryset = HomeInfo.objects.all()
    serializer_class = HomeInfoSerializer

    def get_object(self):
        return self.queryset.first()


class HomeInfoCreateView(generics.CreateAPIView):
    queryset = HomeInfo.objects.all()
    serializer_class = HomeInfoCreateSerializer
    permission_classes = (ManagerPermission, )

    def perform_create(self, serializer):
        return serializer.save()


class HomeInfoUpdateView(generics.UpdateAPIView):
    queryset = HomeInfo.objects.all()
    serializer_class = HomeInfoUpdateSerializer
    permission_classes = (ManagerObjectPermission,)
    lookup_field = "id"

    def get_object(self):
        return self.queryset.first()

    def perform_update(self, serializer):
        return serializer.save()


class HomeInfoDeleteView(generics.DestroyAPIView):
    queryset = HomeInfo.objects.all()
    serializer_class = HomeInfoDeleteSerializer
    permission_classes = (ManagerObjectPermission, )
    lookup_field = "id"

    def get_object(self):
        return self.queryset.first()


class AboutInfoView(generics.RetrieveAPIView):
    queryset = AboutInfo.objects.all()
    serializer_class = AboutInfoSerializer

    def get_object(self):
        return self.queryset.first()


class AboutInfoCreateView(generics.CreateAPIView):
    queryset = AboutInfo.objects.all()
    serializer_class = AboutInfoCreateSerializer
    permission_classes = (ManagerPermission, )

    def perform_create(self, serializer):
        return serializer.save()


class AboutInfoUpdateView(generics.UpdateAPIView):
    queryset = AboutInfo.objects.all()
    serializer_class = AboutInfoUpdateSerializer
    permission_classes = (ManagerObjectPermission, )
    lookup_field = "id"

    def get_object(self):
        return self.queryset.first()

    def perform_update(self, serializer):
        return serializer.save()


class AboutInfoDeleteView(generics.DestroyAPIView):
    queryset = AboutInfo.objects.all()
    serializer_class = AboutInfoDeleteSerializer
    permission_classes = (ManagerObjectPermission, )

    def get_object(self):
        return self.queryset.first()


class DifferentInfoView(generics.ListAPIView):
    queryset = DifferentInfo.objects.all()
    serializer_class = DifferentInfoSerializer


class DifferentInfoCreateView(generics.CreateAPIView):
    queryset = DifferentInfo.objects.all()
    serializer_class = DifferentInfoCreateSerializer
    permission_classes = (ManagerPermission, )

    def perform_create(self, serializer):
        return serializer.save()


class DifferentInfoUpdateView(generics.UpdateAPIView):
    queryset = DifferentInfo.objects.all()
    serializer_class = DifferentInfoUpdateSerializer
    permission_classes = (ManagerObjectPermission, )
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save()


class DifferentInfoDeleteView(generics.DestroyAPIView):
    queryset = DifferentInfo.objects.all()
    serializer_class = DifferentInfoDeleteSerializer
    permission_classes = (ManagerObjectPermission, )
    lookup_field = "id"


class SocialMediaView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class SocialMediaCreateView(generics.CreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaCreateSerializer
    permission_classes = (ManagerPermission, )

    def perform_create(self, serializer):
        return serializer.save()


class SocialMediaUpdateView(generics.UpdateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaUpdateSerializer
    permission_classes = (ManagerObjectPermission, )
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save()


class SocialMediaDeleteView(generics.DestroyAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaDeleteSerializer
    permission_classes = (ManagerObjectPermission, )
    lookup_field = "id"


class ContactInfoView(generics.RetrieveAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

    def get_object(self):
        return ContactInfo.objects.first()


class ContactInfoCreateView(generics.CreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoCreateSerializer
    permission_classes = (ManagerPermission, )

    def perform_create(self, serializer):
        return serializer.save()


class ContactInfoUpdateView(generics.UpdateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoUpdateSerializer
    permission_classes = (ManagerObjectPermission, )
    lookup_field = "id"

    def get_object(self):
        return ContactInfo.objects.first()

    def perform_update(self, serializer):
        return serializer.save()


class ContactInfoDeleteView(generics.DestroyAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoDeleteSerializer
    permission_classes = (ManagerObjectPermission, )
    lookup_field = "id"

    def get_object(self):
        return ContactInfo.objects.first()


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
    permission_classes = (ManagerPermission, )


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        request_type = serializer.validated_data.get('request_type')
        message = serializer.validated_data.get('message')

        # send mail to manager
        send_mail(
            subject=request_type,
            message=message,
            from_email='settings.EMAIL_HOST_USER',
            recipient_list=['yourmail@gmail.com']
        )

        return Response(status=201)


class ContactDeleteView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDeleteSerializer
    permission_classes = (ManagerPermission, )
    lookup_field = "id"
