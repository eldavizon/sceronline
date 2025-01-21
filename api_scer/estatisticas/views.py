from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'estatisticas/index.html')
    
def staff(request):
    return render(request, 'estatisticas/staff.html')

def produtos(request):
    return render(request, 'estatisticas/produtos.html')

def retirada(request):
    return render(request, 'estatisticas/retirada.html')
