from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # blog
    path('blog-list/', views.BlogListView.as_view(), name='blog-list'),
    path('blog-detail/<slug:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog-create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog-update/<slug:slug>/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog-delete/<slug:slug>/', views.BlogDeleteView.as_view(), name='blog-delete'),

    # blog comment
    path('blog-comment-list/', views.BlogCommentListView.as_view(), name='blog-comment-list'),
    path('blog-comment-create/', views.BlogCommentCreateView.as_view(), name='blog-comment-create'),
    path('blog-comment-update/<int:id>/', views.BlogCommentUpdateView.as_view(), name='blog-comment-update'),
    path('blog-comment-delete/<int:id>/', views.BlogCommentDeleteView.as_view(), name='blog-comment-delete'),

    # news
    path('news-list/', views.NewsListView.as_view(), name='news-list'),
    path('news-detail/<slug:slug>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('news-create/', views.NewsCreateView.as_view(), name='news-create'),
    path('news-update/<slug:slug>/', views.NewsUpdateView.as_view(), name='news-update'),
    path('news-delete/<slug:slug>/', views.NewsDeleteView.as_view(), name='news-delete'),

    # gallery
    path('gallery-list/', views.GalleryListView.as_view(), name='gallery-list'),
    path('gallery-create/', views.GalleryCreateView.as_view(), name='gallery-create'),
    path('gallery-delete/<int:id>/', views.GalleryDeleteView.as_view(), name='gallery-delete'),

    # pastime
    path('pastime-list/', views.PastimeListView.as_view(), name='pastime-list'),
    path('pastime-create/', views.PastimeCreateView.as_view(), name='pastime-create'),
    path('pastime-update/<int:id>/', views.PastimeUpdateView.as_view(), name='pastime-update'),
    path('pastime-delete/<int:id>/', views.PastimeDeleteView.as_view(), name='pastime-delete'),
]
