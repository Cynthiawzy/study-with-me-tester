from django.urls import path
from .views import VideoPreferenceListCreateView, VideoPreferenceDetailView, VideoPreferenceDelete

urlpatterns = [
    path('video-preferences/', VideoPreferenceListCreateView.as_view(), name='video-preference-list-create'),
    path('video-preferences/<int:pk>/', VideoPreferenceDetailView.as_view(), name='video-preference-detail'),
    path('video-preferences/delete/<int:id>/', VideoPreferenceDelete.as_view(), name="delete-video-preference"),
]