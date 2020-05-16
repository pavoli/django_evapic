from django.shortcuts import render

# Create your views here.
from .models import *


def home(request):
    context = {

    }

    return render(request, 'pic_store/main.html', context)


def pictures(request):
    context = {

    }

    return render(request, 'pic_store/pictures.html', context)