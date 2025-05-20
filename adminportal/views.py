from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, format=None):
        # You can pass additional context data to your template by adding it to the context dict.
        context = {}
        return Response(context)
