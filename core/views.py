from django.shortcuts import render # type: ignore

from core.models import Produto


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': "Web progamming with Django Framework",
        'other': "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.",
        'produtos' : produtos
    }
    return render(request, 'index.html' , context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    prod = Produto.objects.get(id=pk)#vai buscar o produto pelo id
    
    context = {
        'produto': prod
    } 
    return render(request, 'produto.html', context)
