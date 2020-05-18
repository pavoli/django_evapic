from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *


def home(request):
    context = {

    }

    return render(request, 'pic_store/home.html', context)


def pictures(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pictures')
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    context = {
        'form': form,
        'documents': documents,
    }

    return render(request, 'pic_store/pictures.html', context)


def about(request):
    context = {
    }

    return render(request, 'pic_store/about.html', context)
