from django.urls import path

from .views import SearchResultsView

urlpatterns = [
    path('', SearchResultsView.as_view(), name='search'),
]