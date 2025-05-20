from django.urls import path
from .views import *

urlpatterns = [
    path('base/',IndexView.as_view(),name="base"),

]