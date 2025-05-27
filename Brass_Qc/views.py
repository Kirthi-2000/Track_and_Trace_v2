from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render

# Create your views here.

class BrassPickTableView(APIView):
    def get(self, request):
        return render(request, 'Brass_Qc/Brass_PickTable.html')
    
class IqfPickTableView(APIView):
    def get(self, request):
        return render(request, 'IQF/Iqf_PickTable.html')
    
class IqpRejectTableView(APIView):
    def get(self, request):
        return render(request, 'IQF/Iqp_RejectTable.html')