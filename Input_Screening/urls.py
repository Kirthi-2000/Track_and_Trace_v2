from django.urls import path
from .views import *

urlpatterns = [
    path('IS_PickTable/', IS_PickTable.as_view(), name='IS_PickTable'),
    path('IS_AcceptTable.html/', IS_AcceptTable.as_view(), name='IS_AcceptTable'),
    path('IS_RejectTable/', IS_RejectTable.as_view(), name='IS_RejectTable'),
    path('Recovery_IS_PickTable/', Recovery_IS_PickTable.as_view(), name='Recovery_IS_PickTable'),
    path('Recovery_IS_AcceptTable/', Recovery_IS_AcceptTable.as_view(), name='Recovery_IS_AcceptTable'),
    path('Recovery_IS_RejectTable/', Recovery_IS_RejectTable.as_view(), name='Recovery_IS_RejectTable'),

]