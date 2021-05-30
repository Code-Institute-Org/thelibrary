from django.urls import path

from .views import manager_view, profile_search

urlpatterns = [
    path('', manager_view, name='manager'),
    path('users/', profile_search, name='profile_search'),
]
