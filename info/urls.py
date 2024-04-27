from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('about/', views.AboutInfoView.as_view(), name='about'),
    path('different/', views.DifferentInfoView.as_view(), name='different'),
    path('contact-info/', views.ContactInfoView.as_view(), name='contact-info'),
    path('social-media/', views.SocialMediaView.as_view(), name='social-media'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
