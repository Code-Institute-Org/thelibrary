from django.urls import path

from .views import (
    manager_view,
    profile_search,
    ManageUserProfile,
    manage_categories,
    EditCategory,
)

urlpatterns = [
    path('', manager_view, name='manager'),
    path('users/', profile_search, name='profile_search'),
    path(
        'manage_user/<int:pk>',
        ManageUserProfile.as_view(), name='manage_user'),
    path(
        'manage_categories/',
        manage_categories, name='manage_categories'),
    path(
        'edit_category/<int:pk>',
        EditCategory.as_view(), name='edit_category'),
]
