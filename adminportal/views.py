from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render

class BaseView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def get(self, request, format=None):
        # You can pass additional context data to your template by adding it to the context dict.
        context = {}
        return Response(context)

class IndexView1(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Dashboard/index.html'

    def get(self, request, format=None):
        # You can pass additional context data to your template by adding it to the context dict.
        context = {}
        return Response(context)

