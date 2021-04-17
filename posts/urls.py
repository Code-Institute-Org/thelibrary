from django.urls import path

from .views import PostDetailView, AllPostsView, CreatePostView, ReviewPostsView

urlpatterns = [
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('all_posts/', AllPostsView.as_view(), name='all_posts'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('review_posts/', ReviewPostsView.as_view(), name='review_posts'),
]