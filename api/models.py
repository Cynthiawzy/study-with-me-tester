from django.db import models
from django.contrib.auth.models import User

class VideoPreference(models.Model):
    MOOD_CHOICES = [
        ('lofi', 'Lofi'),
        ('nature', 'Nature'),
        ('coffee shop', 'Coffee Shop'),
        ('idol', 'Idol'),
        ('typing', 'Typing'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    video_url = models.URLField()
    title = models.CharField(max_length=255)
    thumbnail_url = models.URLField(blank=True, null=True)


