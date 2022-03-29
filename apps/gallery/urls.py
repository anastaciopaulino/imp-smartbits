from django.urls import path
from .views import GallaryListView

app_name = 'gallery'

urlpatterns = [
    path('', GallaryListView.as_view(), name='gallery'),
]
