from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # blog
    path('blog-list/', views.BlogListView.as_view(), name='blog-list'),
    path('blog-detail/<slug:slug>/', views.BlogDetailView.as_view(), name='blog-create'),
    path('blog-create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog-update/<slug:slug>/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog-delete/<slug:slug>/', views.BlogDeleteView.as_view(), name='blog-delete'),

    # blog comment
    path('blog-comment-list/', views.BlogCommentListView.as_view(), name='blog-comment-list'),
    path('blog-comment-create/', views.BlogCommentCreateView.as_view(), name='blog-comment-create'),
    path('blog-comment-update/<int:id>/', views.BlogCommentUpdateView.as_view(), name='blog-comment-update'),
    path('blog-comment-delete/<int:id>/', views.BlogCommentDeleteView.as_view(), name='blog-comment-delete'),
]
