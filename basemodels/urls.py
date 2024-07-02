from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("country-list/", views.CountryListView.as_view(), name="country-list"),
    path("city-list/", views.CityListView.as_view(), name="city-list"),
]
