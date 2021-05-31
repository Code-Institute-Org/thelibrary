from django.urls import path

from .views import (
    manager_view,
    profile_search,
    ManageUserProfile,
    manage_categories,
    EditCategory,
    manage_channels,
    EditChannel,
    manage_tags,
    EditTag,
    delete_tag,
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
    path(
        'manage_channels/',
        manage_channels, name='manage_channels'),
    path(
        'edit_channel/<int:pk>',
        EditChannel.as_view(), name='edit_channel'),
    path(
        'manage_tags/',
        manage_tags, name='manage_tags'),
    path(
        'edit_tag/<int:pk>',
        EditTag.as_view(), name='edit_tag'),
    path('delete_tag/<int:pk>', delete_tag, name="delete_tag")
]
