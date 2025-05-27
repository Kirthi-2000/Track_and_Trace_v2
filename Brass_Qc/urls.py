from django.urls import path
from .views import *

urlpatterns = [
    path('brass_picktable/', BrassPickTableView.as_view(), name='BrassPickTableView'),
    path('iqf_picktable/', IqfPickTableView.as_view(), name='IqfPickTableView'),
    path('iqp_rejecttable/', IqpRejectTableView.as_view(), name='IqpRejectTableView'),
]