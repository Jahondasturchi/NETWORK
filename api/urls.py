from django.urls import path

from .views import *

urlpatterns = [
    path('profiles/', ProfileListApiVeiw.as_view(), name='profiles'),
    path('posts/', PostListApiVeiw.as_view(), name='posts'),
    path('profiles/<int:pk>', ProfileRetry.as_view(), name='posts_update'),
    path('posts/<int:pk>', PostRetry.as_view(), name='profiles_update'),
   
]