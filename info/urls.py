from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    # home info
    path('home/', views.HomeInfoView.as_view(), name='home'),
    path('home-create/', views.HomeInfoCreateView.as_view(), name='home-create'),
    path('home-update/<int:id>/', views.HomeInfoUpdateView.as_view(), name='home-update'),
    path('home-delete/<int:id>/', views.HomeInfoDeleteView.as_view(), name='home-delete'),

    # home special offer
    path('special-offer-list/', views.SpecialOfferListView.as_view(), name='special-offer-list'),
    path('special-offer-detail/<slug:slug>/', views.SpecialOfferDetailView.as_view(), name='special-offer-detail'),
    path('special-offer-create/', views.SpecialOfferCreateView.as_view(), name='special-offer-create'),
    path('special-offer-update/<slug:slug>/', views.SpecialOfferUpdateView.as_view(), name='special-offer-update'),
    path('special-offer-delete/<slug:slug>/', views.SpecialOfferDeleteView.as_view(), name='special-offer-delete'),

    # about info
    path('about/', views.AboutInfoView.as_view(), name='about'),
    path('about-create/', views.AboutInfoCreateView.as_view(), name='about-create'),
    path('about-update/<int:id>/', views.AboutInfoUpdateView.as_view(), name='about-update'),
    path('about-delete/<int:id>/', views.AboutInfoDeleteView.as_view(), name='about-delete'),

    # about different info
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

    # partnership feature info
    path('partnership-feature-list/', views.PartnershipFeatureInfoListView.as_view(), name='partnership-feature-list'),
    path('partnership-feature-create/', views.PartnershipFeatureInfoCreateView.as_view(), name='partnership-feature-create'),
    path('partnership-feature-update/<int:id>/', views.PartnershipFeatureInfoUpdateView.as_view(), name='partnership-feature-update'),
    path('partnership-feature-delete/<int:id>/', views.PartnershipFeatureInfoDeleteView.as_view(), name='partnership-feature-delete'),

    # partnership type info
    path('partnership-type-list/', views.PartnershipTypeInfoListView.as_view(), name='partnership-type-list'),
    path('partnership-type-create/', views.PartnershipTypeInfoCreateView.as_view(), name='partnership-type-create'),
    path('partnership-type-update/<int:id>/', views.PartnershipTypeInfoUpdateView.as_view(), name='partnership-type-update'),
    path('partnership-type-delete/<int:id>/', views.PartnershipTypeInfoDeleteView.as_view(), name='partnership-type-delete'),

    # partnership commission info
    path('partnership-commission-list/', views.PartnershipCommissionInfoListView.as_view(), name='partnership-feature-list'),
    path('partnership-commission-create/', views.PartnershipCommissionInfoCreateView.as_view(), name='partnership-commission-create'),
    path('partnership-commission-update/<int:id>/', views.PartnershipCommissionInfoUpdateView.as_view(), name='partnership-commission-update'),
    path('partnership-commission-delete/<int:id>/', views.PartnershipCommissionInfoDeleteView.as_view(), name='partnership-commission-delete'),

    # partnership faq info
    path('partnership-faq-list/', views.PartnershipFaqInfoListView.as_view(), name='partnership-faq-list'),
    path('partnership-faq-create/', views.PartnershipFaqInfoCreateView.as_view(), name='partnership-faq-create'),
    path('partnership-faq-update/<int:id>/', views.PartnershipFaqInfoUpdateView.as_view(), name='partnership-faq-update'),
    path('partnership-faq-delete/<int:id>/', views.PartnershipFaqInfoDeleteView.as_view(), name='partnership-faq-delete'),
]
