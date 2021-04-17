from django.urls import path

from .views import (
    PostDetailView,
    AllPostsView,
    CreatePostView,
    ReviewPostsView,
    approve_post,
    ReviewPostView
)

urlpatterns = [
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('all_posts/', AllPostsView.as_view(), name='all_posts'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('review_posts/', ReviewPostsView.as_view(), name='review_posts'),
    path('review_post/<slug:slug>/', ReviewPostView.as_view(), name='review_post'),
    path('approve/<int:pk>', approve_post, name='approve_post'),
    path('deactivate/<int:pk>', approve_post, name='deactivate_post'),
]