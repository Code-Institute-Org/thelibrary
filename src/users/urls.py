from django.urls import path

from .views import (
    user_profile_view,
    dashboard_view,
    bookmarks_view,
    UserSettingsView,
    UpdateProfileView,
)

urlpatterns = [
    path('<int:pk>/', user_profile_view, name='user_profile'),
    path(
        '<int:pk>/update/',
        UpdateProfileView.as_view(), name='update_profile'),
    path('<int:pk>/settings/', UserSettingsView.as_view(), name="settings"),
    path('bookmarks/', bookmarks_view, name="bookmarks"),
    path('dashboard/', dashboard_view, name="dashboard"),
]
