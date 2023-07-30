from django.urls import path
from .views import ToolsAPI, SingleToolAPI, test_db
from .views import subscribe_newsletter

urlpatterns = [
    path('api/tools/', ToolsAPI.as_view(), name='tools-api'),
    path('api/tools/<int:pk>/', SingleToolAPI.as_view(), name='single-tool-api'),  # New line
    path('test_db/', test_db, name='test_db'),
    path('subscribe_newsletter/', subscribe_newsletter, name='subscribe_newsletter'),
]

