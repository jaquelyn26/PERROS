from django.shortcuts import render

# Create your views here.
def perro(request):
    return render(request, 'index.html')