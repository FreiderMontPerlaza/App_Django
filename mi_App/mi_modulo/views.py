from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pagina_1(request):
    return HttpResponse("<h1>Probando pagina</h1>")

def pagina_2(request):
    imagen = 'https://mi_imagen.jpg'
    parrafo = 'mi_parrafo'
    
    contexto = {
        'imagen':imagen,
        'parrafo':parrafo,

    }

    return render(request,'mi_modulo/pagina_2.html',contexto)


def pagina_3(request):
    return render(request,'mi_modulo/pagina_3.html',{})
