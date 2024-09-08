from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import VideoPreferenceSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import VideoPreference
import requests 
from django.conf import settings


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    
class VideoPreferenceListCreateView(generics.ListCreateAPIView):
    serializer_class = VideoPreferenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = VideoPreference.objects.filter(user=self.request.user)
        mood = self.request.query_params.get('mood', None)
        if mood:
            queryset = queryset.filter(mood=mood)
        return queryset
    
    def fetch_youtube_video_url(self, mood):
        youtube_api_key = settings.YOUTUBE_API_KEY
        search_url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": f"{mood} study with me",
            "key": youtube_api_key,
            "type": "video",
            "maxResults": 1
        }
        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            items = response.json().get("items")
            if items:
                video_id = items[0]["id"]["videoId"]
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                video_title = items[0]["snippet"]["title"]
                return video_url, video_title
        return None, None

    def perform_create(self, serializer):
        if serializer.is_valid():
            mood = serializer.validated_data.get('mood')
            video_url, video_title = self.fetch_youtube_video_url(mood)

            if video_url and video_title:
                serializer.save(user=self.request.user, video_url=video_url, title=video_title)
            else:
                print("Failed to fetch video URL")
        else:
            print(serializer.errors)
            
            
class VideoPreferenceDelete(generics.DestroyAPIView):
    serializer_class = VideoPreferenceSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def get_queryset(self):
        user = self.request.user
        return VideoPreference.objects.filter(user=user)
            
            
class VideoPreferenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideoPreferenceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return VideoPreference.objects.filter(user=self.request.user)
    
