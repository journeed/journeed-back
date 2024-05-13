from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    # home info
    path('home/', views.HomeInfoView.as_view(), name='home'),
    path('home-create/', views.HomeInfoCreateView.as_view(), name='home-create'),
    path('home-update/<int:id>/', views.HomeInfoUpdateView.as_view(), name='home-update'),
    path('home-delete/<int:id>/', views.HomeInfoDeleteView.as_view(), name='home-delete'),

    # about info
    path('about/', views.AboutInfoView.as_view(), name='about'),
    path('about-create/', views.AboutInfoCreateView.as_view(), name='about-create'),
    path('about-update/<int:id>/', views.AboutInfoUpdateView.as_view(), name='about-update'),
    path('about-delete/<int:id>/', views.AboutInfoDeleteView.as_view(), name='about-delete'),

    # different info
    path('different/', views.DifferentInfoView.as_view(), name='different'),
    path('different-create/', views.DifferentInfoCreateView.as_view(), name='different-create'),
    path('different-update/<int:id>/', views.DifferentInfoUpdateView.as_view(), name='different-update'),
    path('different-delete/<int:id>/', views.DifferentInfoDeleteView.as_view(), name='different-delete'),

    # contact info
    path('contact-info/', views.ContactInfoView.as_view(), name='contact-info'),
    path('contact-info-create/', views.ContactInfoCreateView.as_view(), name='contact-info-create'),
    path('contact-info-update/<int:id>/', views.ContactInfoUpdateView.as_view(), name='contact-info-update'),
    path('contact-info-delete/<int:id>/', views.ContactInfoDeleteView.as_view(), name='contact-info-delete'),

    # social media info
    path('social-media/', views.SocialMediaView.as_view(), name='social-media'),
    path('social-media-create/', views.SocialMediaCreateView.as_view(), name='social-media-create'),
    path('social-media-update/<int:id>/', views.SocialMediaUpdateView.as_view(), name='social-media-update'),
    path('social-media-delete/<int:id>/', views.SocialMediaDeleteView.as_view(), name='social-media-delete'),

    # contact
    path('contact-list/', views.ContactListView.as_view(), name='contact-list'),
    path('contact-create/', views.ContactCreateView.as_view(), name='contact-create'),
    path('contact-delete/<int:id>/', views.ContactDeleteView.as_view(), name='contact-delete'),
]
