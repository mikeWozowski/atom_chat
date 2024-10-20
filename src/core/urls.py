from django.urls import path, include

urlpatterns = [
    path('', include('chat.urls.templates')),
    path('api/', include('chat.urls.api')),
]
