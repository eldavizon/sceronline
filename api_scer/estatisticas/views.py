from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Produto, Retirada
from .forms import ProdutoForm, RetiradaForm
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def index(request):
    
    retiradas = Retirada.objects.all()
    
    if request.method == "POST":
        form = RetiradaForm(request.POST)
        
        if form.is_valid():
            
            instance = form.save(commit=False) # Não se salva o formulario imediatamente para que seja possivel adicionar o usuario
            instance.staff = request.user   # Adiciona-se o usuário às informações do formulario aqui
            instance.save()     #Agora sim, pode-se salvar.
            
            return redirect('estatisticas-index')
        
    else:
        form = RetiradaForm()
    
    context = {
        'retiradas':retiradas,
        'form': form,
    }
    
    return render(request, 'estatisticas/index.html', context)



@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def staff(request):
    
    workers = User.objects.all()
    
    context = {
        'workers' : workers,
    }
    
    return render(request, 'estatisticas/staff.html', context)



@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def staff_detail(request, pk):
    
    workers = User.objects.get(id = pk)
    
    context = {
                'workers' : workers
    }

    return render(request, 'estatisticas/staff_detail.html', context)

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
def produtos_delete(request, pk):
    
    item = Produto.objects.get(id = pk)
    
    if request.method=="POST":
        item.delete()
        return redirect('estatisticas-produtos')
    
    return render(request, 'estatisticas/produtos_delete.html')



@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def produtos_update(request, pk):
    
    item = Produto.objects.get(id = pk)
        
    if request.method=="POST":
        form = ProdutoForm(request.POST, instance = item)
        
        if form.is_valid():
            form.save()
            return redirect('estatisticas-produtos')        
    else:
        form = ProdutoForm(instance = item)
        
    context = {
        'form': form, 
    }
    
    return render(request, 'estatisticas/produtos_update.html', context)



@login_required(login_url='user-login', ) # está configurado nas settings > login_url.
def retirada(request):
    
    retiradas = Retirada.objects.all()
    
    context = {
        'retiradas' : retiradas,
    }
    
    return render(request, 'estatisticas/retirada.html', context)
