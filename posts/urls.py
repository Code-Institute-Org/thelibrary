from django.urls import path

from .views import (
    PostDetailView,
    AllPostsView,
    CreatePostView,
    ReviewPostsView,
    approve_post,
    delete_post,
    ReviewPostView,
    EditPostView
)

urlpatterns = [
    path('post/<int:pk>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('all_posts/', AllPostsView.as_view(), name='all_posts'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('review_posts/', ReviewPostsView.as_view(), name='review_posts'),
    path('review_post/<int:pk>/<slug:slug>/', ReviewPostView.as_view(), name='review_post'),
    path('approve/<int:pk>/<slug:slug>/', approve_post, name='approve_post'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('edit/<int:pk>/<slug:slug>/', EditPostView.as_view(), name='edit_post'),
]