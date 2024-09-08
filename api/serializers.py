from django.contrib.auth.models import User
from rest_framework import serializers
from .models import VideoPreference

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class VideoPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPreference
        fields = ["id", "user", "mood", "video_url", "video_id", "title", "thumbnail_url"]
        read_only_fields = ["user"]