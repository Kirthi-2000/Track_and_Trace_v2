from django.urls import path
from .views import *

urlpatterns = [
    path('baseview/',BaseView.as_view(),name="baseview"),
    path('base/',IndexView.as_view(),name="base"),
    path('BulkUpload/',BulkUpload.as_view(),name="BulkUpload"),

]