from rest_framework import serializers
from .models import AITool, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image_url']

class AIToolSerializer(serializers.ModelSerializer):
    explanation_photos = PhotoSerializer(many=True, read_only=True)
    full_favicon_url = serializers.CharField(read_only=True)

    class Meta:
        model = AITool
        fields = '__all__'
