from django.urls import path
from . import views

app_name = 'partnership'

urlpatterns = [
    # partnership application
    path('application-list/', views.ApplicationListView.as_view(), name='application-list'),
    path('application-create/', views.ApplicationCreateView.as_view(), name='application-create'),
    path('application-update/<int:id>/', views.ApplicationUpdateView.as_view(), name='application-update'),
    path('application-delete/<int:id>/', views.ApplicationDeleteView.as_view(), name='application-delete'),
]
