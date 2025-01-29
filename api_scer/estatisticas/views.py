from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdutoForm

# Create your views here.

@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def index(request):
    return render(request, 'estatisticas/index.html')

@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def staff(request):
    return render(request, 'estatisticas/staff.html')

@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def produtos(request):
    
    items = Produto.objects.all()
    #    items = Produto.objects.raw() significaria usar o código SQL bruto ao invés do ORM.

    if request.method=="POST":
        form = ProdutoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('estatisticas-produtos')
    else:
        form = ProdutoForm()
    
        
    context= {
        'items': items,
        'form' : form,
    }
    
    return render(request, 'estatisticas/produtos.html', context)

@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def retirada(request):
    return render(request, 'estatisticas/retirada.html')
