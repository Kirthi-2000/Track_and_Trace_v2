from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

class BaseView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def get(self, request, format=None):
        # You can pass additional context data to your template by adding it to the context dict.
        context = {}
        return Response(context)

class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Dashboard/index.html'

    def get(self, request, format=None):
        # You can pass additional context data to your template by adding it to the context dict.
        context = {}
        return Response(context)

class BulkUpload(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Day_Planning/DP_BulkUpload.html'

    def get(self, request, format=None):
        # You can pass additional context data to your template by adding it to the context dict.
        context = {}
        return Response(context)