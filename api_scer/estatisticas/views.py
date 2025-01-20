from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Essa é a página inicial - index")

def staff(request):
    return HttpResponse("Página de staff")