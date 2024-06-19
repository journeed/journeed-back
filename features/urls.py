from django.urls import path
from . import views

urlpatterns = [
    # Story
    path('story-list/', views.StoryListView.as_view(), name='story-list'),
    path('story-create/', views.StoryCreateView.as_view(), name='story-create'),
    path('story-update/<int:id>/', views.StoryUpdateView.as_view(), name='story-update'),
    path('story-detail/<int:id>/', views.StoryDetailView.as_view(), name='story-detail'),
    path('story-delete/<int:id>/', views.StoryDeleteView.as_view(), name='story-delete'),

    # Story Comment
    path('story-comment-list/', views.StoryCommentListView.as_view(), name='story-comment-list'),
    path('story-comment-create/', views.StoryCommentCreateView.as_view(), name='story-comment-create'),
    path('story-comment-update/<int:id>/', views.StoryCommentUpdateView.as_view(), name='story-comment-update'),
    path('story-comment-delete/<int:id>/', views.StoryCommentDeleteView.as_view(), name='story-comment-delete'),

    # Like
    path('story-like-list/', views.StoryLikeListView.as_view(), name='story-comment-like'),
    path('story-like-create/', views.StoryLikeCreateView.as_view(), name='story-like-create'),
    path('story-comment-like-list/', views.StoryCommentLikeListView.as_view(), name='story-comment-like'),
    path('story-comment-like-create/', views.StoryCommentLikeCreateView.as_view(), name='story-comment-like-create'),
]

