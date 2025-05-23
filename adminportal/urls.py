from django.urls import path
from .views import *

urlpatterns = [
    path('baseview/',BaseView.as_view(),name="baseview"),
    path('base/',IndexView1.as_view(),name="base"),
]