from django.urls import path

from .views import (
    user_profile_view,
    UserSettingsView
)

urlpatterns = [
    path('<int:pk>/', user_profile_view, name='user_profile'),
    path('settings/<int:pk>', UserSettingsView.as_view(), name="settings")
]