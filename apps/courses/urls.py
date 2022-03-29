from django.urls import path
from .views import CourseListView, SubscriptionCreateView, Success

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='courses'),
    path('subscription/', SubscriptionCreateView.as_view(), name='subscription'),
    path('success/', Success.as_view(), name='success')
]
