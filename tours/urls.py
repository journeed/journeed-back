from django.urls import path
from . import views

app_name = "tours"

urlpatterns = [
    # tour
    path('tour-list/', views.TourListView.as_view(), name="tour-list"),
    path('tour-detail/<slug:slug>/', views.TourDetailView.as_view(), name="tour-detail"),
    path('tour-create/', views.TourCreateView.as_view(), name="tour-create"),
    path('tour-update/<slug:slug>/', views.TourUpdateView.as_view(), name="tour-update"),
    path('tour-delete/<slug:slug>/', views.TourDeleteView.as_view(), name="tour-delete"),

    # tour review
    path('tour-review-list/', views.TourReviewListView.as_view(), name="tour-review-list"),
    path('tour-review-create/', views.TourReviewCreateView.as_view(), name="tour-review-create"),
    path('tour-review-update/<int:id>/', views.TourReviewUpdateView.as_view(), name="tour-review-update"),
    path('tour-review-delete/<int:id>/', views.TourReviewDeleteView.as_view(), name="tour-review-delete"),
]

