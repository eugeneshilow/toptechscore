from django.urls import path
from .views import ToolsAPI, test_db

urlpatterns = [
    path('api/tools/', ToolsAPI.as_view(), name='tools-api'),
    path('test_db/', test_db, name='test_db'),
]
