from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from .models import *
from services.permission import ManagerPermission


class ApplicationListView(generics.ListAPIView):
    queryset = PartnershipApplication.objects.all()
    serializer_class = ApplicationListSerializer
    permission_classes = (ManagerPermission, )


class ApplicationCreateView(generics.CreateAPIView):
    queryset = PartnershipApplication.objects.all()
    serializer_class = ApplicationCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        company_name = serializer.validated_data.get('company_name')
        message = serializer.validated_data.get('message')

        # send mail to manager
        send_mail(
            subject=company_name,
            message=message,
            from_email='settings.EMAIL_HOST_USER',
            recipient_list=['yourmail@gmail.com']
        )

        return Response(status=201)


class ApplicationDeleteView(generics.DestroyAPIView):
    queryset = PartnershipApplication.objects.all()
    serializer_class = ApplicationDeleteSerializer
    permission_classes = (ManagerPermission, )
    lookup_field = "id"

