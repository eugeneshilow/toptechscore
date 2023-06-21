from django.http import HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AITool
from .serializers import AIToolSerializer
from django.db import connection

class ToolsAPI(APIView):
    def get(self, request, format=None):
        tools = AITool.objects.all()
        serializer = AIToolSerializer(tools, many=True)
        return Response(serializer.data)
    
class HomePageView(View):
    def get(self, request):
        return HttpResponse("This is the home page")
    
def test_db(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        row = cursor.fetchone()
    return HttpResponse(f"Database connection test: {row}")
