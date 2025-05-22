from django.urls import path
from .views import *

urlpatterns = [
    path('baseview/',BaseView.as_view(),name="baseview"),
    path('base/',IndexView.as_view(),name="base"),
    path('BulkUpload/',BulkUpload.as_view(),name="BulkUpload"),
<<<<<<< HEAD
    
    path('Table/',Table.as_view(),name="Table"),
=======

>>>>>>> 6a115c35b015e2066e771829a77eab252b59303b
]