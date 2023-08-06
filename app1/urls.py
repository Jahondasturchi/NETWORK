from django.urls import path
from .views import dashboard, allprofiles, profile

app_name = "app1"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path('allprofiles/', allprofiles, name='allprofiles'),
    path('profile/<int:pk>/',profile, name='profile')
]