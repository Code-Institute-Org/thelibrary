from django.urls import path

from .views import PostDetailView, AllPostsView

urlpatterns = [
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('all_posts/', AllPostsView.as_view(), name='all_posts')
]