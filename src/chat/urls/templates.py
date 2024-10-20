from django.urls import path
from chat.views.templates import ChatTemplateAsyncViewSet

urlpatterns = [
    path('', ChatTemplateAsyncViewSet.as_view({"get": "get_main_page"}), name='main_page'),
    path('auth/', ChatTemplateAsyncViewSet.as_view({"get": "get_auth_page"}), name='auth_page'),
]