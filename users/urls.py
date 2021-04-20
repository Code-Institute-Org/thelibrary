from django.urls import path

from .views import (
    user_profile_view,
    UserSettingsView,
    user_bookmarks_view,
    UpdateProfileView,
    PostsByAuthorView,
)

urlpatterns = [
    path('<int:pk>/', user_profile_view, name='user_profile'),
    path('<int:pk>/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('<int:pk>/settings/', UserSettingsView.as_view(), name="settings"),
    path('<int:pk>/bookmarks/', user_bookmarks_view, name="bookmarks"),
    path('<int:pk>/all_posts', PostsByAuthorView.as_view(), name="posts_by_author"),
]