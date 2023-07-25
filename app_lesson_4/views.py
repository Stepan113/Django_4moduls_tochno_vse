from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.

my_list = [randint(-10, 10) for x in range(10)]


def get_hw(request):
    return HttpResponse(f"{my_list}, надеюсь, это сработает")
