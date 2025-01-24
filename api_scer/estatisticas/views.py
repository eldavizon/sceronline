from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def index(request):
    return render(request, 'estatisticas/index.html')

@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def staff(request):
    return render(request, 'estatisticas/staff.html')

@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def produtos(request):
    return render(request, 'estatisticas/produtos.html')

@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def retirada(request):
    return render(request, 'estatisticas/retirada.html')
