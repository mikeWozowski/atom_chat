from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from django.views import View

class ChatTemplateAsyncViewSet(ViewSet):

    @staticmethod
    def get_main_page(request):
        return render(request, "index.html")

    @staticmethod
    def get_auth_page(request):
        return render(request, "auth.html")