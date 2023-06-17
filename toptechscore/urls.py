from django.contrib import admin
from django.urls import include, path
from ai_tools.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tools/', include('ai_tools.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('', include('ai_tools.urls')),
    # other paths...
]

