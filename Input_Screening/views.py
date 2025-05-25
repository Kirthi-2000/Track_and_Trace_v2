from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render

# Create your views here.
class IS_PickTable(APIView):
    def get(self, request):
        return render(request, 'Input_Screening/IS_PickTable.html')
    
class IS_RejectTable(APIView):
    def get(self, request):
        return render(request, 'Input_Screening/IS_RejectTable.html')