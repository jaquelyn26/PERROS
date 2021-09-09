from django.shortcuts import render
from .models import *

# Create your views here.
def perro(request):
    alllibro=libro.objects.all()
    return render(request, 'index.html',{'alllibro':alllibro})

def generic(request):
    return render(request, 'generic.html')

def elements(request):
    return render(request, 'elements.html')
