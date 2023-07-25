from django.urls import path
from .views import get_hw

urlpatterns = [
    path('', get_hw)
]
