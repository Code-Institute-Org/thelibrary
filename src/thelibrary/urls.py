from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('custom_slack_provider.urls')),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('search/', include('search.urls')),
    path('manager/', include('manager.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
