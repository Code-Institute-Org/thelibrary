from django.urls import path

from .views import manager_view

urlpatterns = [
    path('', manager_view, name='manager'),
]
