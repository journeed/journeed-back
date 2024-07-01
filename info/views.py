from rest_framework import generics
from .models import *
from .serializers import *
from services.permission import ManagerPermission, ManagerObjectPermission
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail


# Home Page Info

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


# About Page Info

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


# Social Media Info

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


# Contact Page Info

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


# Contact

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


# Partnership Page Info

class PartnershipFeatureInfoListView(generics.ListAPIView):
    queryset = PartnershipFeatureInfo.objects.all()
    serializer_class = PartnershipFeatureInfoListSerializer


class PartnershipFeatureInfoCreateView(generics.CreateAPIView):
    queryset = PartnershipFeatureInfo.objects.all()
    serializer_class = PartnershipFeatureInfoCreateSerializer
    permission_classes = (ManagerPermission,)

    def perform_create(self, serializer):
        return serializer.save()


class PartnershipFeatureInfoUpdateView(generics.UpdateAPIView):
    queryset = PartnershipFeatureInfo.objects.all()
    serializer_class = PartnershipFeatureInfoUpdateSerializer
    permission_classes = (ManagerPermission,)
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save()


class PartnershipFeatureInfoDeleteView(generics.DestroyAPIView):
    queryset = PartnershipFeatureInfo.objects.all()
    serializer_class = PartnershipFeatureInfoDeleteSerializer
    permission_classes = (ManagerPermission,)
    lookup_field = "id"


class PartnershipTypeInfoListView(generics.ListAPIView):
    queryset = PartnershipTypeInfo.objects.all()
    serializer_class = PartnershipTypeInfoListSerializer


class PartnershipTypeInfoCreateView(generics.CreateAPIView):
    queryset = PartnershipTypeInfo.objects.all()
    serializer_class = PartnershipTypeInfoCreateSerializer
    permission_classes = (ManagerPermission,)

    def perform_create(self, serializer):
        return serializer.save()


class PartnershipTypeInfoUpdateView(generics.UpdateAPIView):
    queryset = PartnershipTypeInfo.objects.all()
    serializer_class = PartnershipTypeInfoUpdateSerializer
    permission_classes = (ManagerPermission,)
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save()


class PartnershipTypeInfoDeleteView(generics.DestroyAPIView):
    queryset = PartnershipTypeInfo.objects.all()
    serializer_class = PartnershipTypeInfoDeleteSerializer
    permission_classes = (ManagerPermission,)
    lookup_field = "id"


class PartnershipCommissionInfoListView(generics.ListAPIView):
    queryset = PartnershipCommissionInfo.objects.all()
    serializer_class = PartnershipCommissionInfoListSerializer


class PartnershipCommissionInfoCreateView(generics.CreateAPIView):
    queryset = PartnershipCommissionInfo.objects.all()
    serializer_class = PartnershipCommissionInfoCreateSerializer
    permission_classes = (ManagerPermission,)

    def perform_create(self, serializer):
        return serializer.save()


class PartnershipCommissionInfoUpdateView(generics.UpdateAPIView):
    queryset = PartnershipCommissionInfo.objects.all()
    serializer_class = PartnershipCommissionInfoUpdateSerializer
    permission_classes = (ManagerPermission,)
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save()


class PartnershipCommissionInfoDeleteView(generics.DestroyAPIView):
    queryset = PartnershipCommissionInfo.objects.all()
    serializer_class = PartnershipCommissionInfoDeleteSerializer
    permission_classes = (ManagerPermission,)
    lookup_field = "id"


class PartnershipFaqInfoListView(generics.ListAPIView):
    queryset = PartnershipFaqInfo.objects.all()
    serializer_class = PartnershipFaqInfoListSerializer


class PartnershipFaqInfoCreateView(generics.CreateAPIView):
    queryset = PartnershipFaqInfo.objects.all()
    serializer_class = PartnershipFaqInfoCreateSerializer
    permission_classes = (ManagerPermission,)

    def perform_create(self, serializer):
        return serializer.save()


class PartnershipFaqInfoUpdateView(generics.UpdateAPIView):
    queryset = PartnershipFaqInfo.objects.all()
    serializer_class = PartnershipFaqInfoUpdateSerializer
    permission_classes = (ManagerPermission,)
    lookup_field = "id"

    def perform_update(self, serializer):
        return serializer.save()


class PartnershipFaqInfoDeleteView(generics.DestroyAPIView):
    queryset = PartnershipFaqInfo.objects.all()
    serializer_class = PartnershipFaqInfoDeleteSerializer
    permission_classes = (ManagerPermission,)
    lookup_field = "id"



