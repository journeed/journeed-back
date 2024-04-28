from rest_framework import generics
from .models import HomeInfo, AboutInfo, DifferentInfo, SocialMedia, ContactInfo, Contact
from .serializers import HomeInfoSerializer, AboutInfoSerializer, DifferentInfoSerializer, SocialMediaSerializer, ContactInfoSerializer, ContactSerializer
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail


class HomeInfoView(generics.RetrieveAPIView):
    queryset = HomeInfo.objects.all()
    serializer_class = HomeInfoSerializer

    def get_object(self):
        return self.queryset.first()


class AboutInfoView(generics.RetrieveAPIView):
    queryset = AboutInfo.objects.all()
    serializer_class = AboutInfoSerializer

    def get_object(self):
        return self.queryset.first()


class DifferentInfoView(generics.ListAPIView):
    queryset = DifferentInfo.objects.all()
    serializer_class = DifferentInfoSerializer


class SocialMediaView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class ContactInfoView(generics.RetrieveAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

    def get_object(self):
        return ContactInfo.objects.first()


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

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




