from django.shortcuts import render # type: ignore

def index(request):
    
    print(dir(request))
    print(F"User: {request.user}")
    
    if str(request.user) == 'AnonymousUser':
        teste = "User is not authenticated"
    else:
        teste = "User is authenticated"
    context = {
        'curso': "Web progamming with Django Framework",
        'other': "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.",
        'logado' : teste
    }
    return render(request, 'index.html' , context)

def contato(request):
    return render(request, 'contato.html')
