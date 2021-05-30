from django.urls import path

from .views import (
    manager_view,
    profile_search,
    ManageUserProfile
)

urlpatterns = [
    path('', manager_view, name='manager'),
    path('users/', profile_search, name='profile_search'),
    path(
        'manage_user/<int:pk>',
        ManageUserProfile.as_view(), name='manage_user'),
]
