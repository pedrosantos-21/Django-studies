from django.shortcuts import render # type: ignore
from django.shortcuts import get_object_or_404
from django.http import HttpResponse # type: ignore
from django.template import loader # type: ignore

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
    #prod = Produto.objects.get(id=pk)#vai buscar o produto pelo id
    prod = get_object_or_404(Produto, id=pk) #vai buscar o produto pelo id ou retorna 404 se não encontrar
    
    context = {
        'produto': prod
    } 
    return render(request, 'produto.html', context)

def error404(request, exception=None):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),content_type='text/html; charsert=utf8', status=404)  

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),content_type='text/html; charsert=utf8', status=500)