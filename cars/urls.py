from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("category/list/", views.CarCategoryListView.as_view(), name="category-list"),
    path("steering/list/", views.SteeringListView.as_view(), name="steering-list"),
    path("fuel/list/", views.FuelListView.as_view(), name="fuel-list"),
    path("list/", views.CarListView.as_view(), name="list"),
    path("detail/<id>/", views.CarDetailView.as_view(), name="detail"),

    path("my/list/", views.MyCarListView.as_view(), name="my-cars-list"),
    path("create/", views.CarCreateView.as_view(), name="car-create"),
    path("edit/<id>/", views.CarEditView.as_view(), name="car-edit"),
    path("review/create/", views.CarReviewCreateView.as_view(), name="create-review"),
    path("review/edit/<id>/", views.CarReviewEditView.as_view(), name="review-edit"),
    path("image/delete/<id>/", views.CarImageDeleteView.as_view(), name="car-image-delete"),
]
