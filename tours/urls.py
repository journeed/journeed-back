from django.urls import path
from . import views

app_name = "tours"

urlpatterns = [
    # tour
    path('tour-list/', views.TourListView.as_view(), name="tour-list"),
    path('tour-detail/<slug:slug>/', views.TourDetailView.as_view(), name="tour-detail"),
    # path('tour-create/'),
    # path('tour-update/<slug:slug>/'),
    # path('tour-delete/<slug:slug>/'),

    # tour review
    path('tour-review-list/', views.TourReviewListView.as_view(), name="tour-review-list"),
]

