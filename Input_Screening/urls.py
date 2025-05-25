from django.urls import path
from .views import *

urlpatterns = [
    path('IS_PickTable/', IS_PickTable.as_view(), name='IS_PickTable'),
    path('IS_RejectTable/', IS_RejectTable.as_view(), name='IS_RejectTable'),

]