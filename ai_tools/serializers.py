from rest_framework import serializers
from .models import AITool

class AIToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = AITool
        fields = '__all__'
