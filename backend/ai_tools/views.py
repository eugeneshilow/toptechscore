from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AITool
from .serializers import AIToolSerializer
from django.db import connection
import requests
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class ToolsAPI(APIView):
    def get(self, request, format=None):
        tools = AITool.objects.all()
        serializer = AIToolSerializer(tools, many=True)
        return Response(serializer.data)

class SingleToolAPI(APIView):
    def get(self, request, pk, format=None):
        try:
            tool = AITool.objects.get(id=pk)
            serializer = AIToolSerializer(tool)
            return Response(serializer.data)
        except AITool.DoesNotExist:
            return Response({'error': 'Tool not found'}, status=404)

class HomePageView(View):
    def get(self, request):
        return HttpResponse("This is the home page")
    
def test_db(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        row = cursor.fetchone()
    return HttpResponse(f"Database connection test: {row}")

@csrf_exempt
def subscribe_newsletter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        if email:
            url = os.getenv("MAILCHIMP_API_ENDPOINT")
            headers = {
                "Content-Type": "application/json",
                "Authorization": f'apikey {os.getenv("MAILCHIMP_API_KEY")}'
            }
            data = {
                "email_address": email,
                "status": "pending"
            }
            response = requests.post(url, headers=headers, json=data)
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({'error': 'No email provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
