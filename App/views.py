from django.shortcuts import render
from models import Servidor
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def index(request, pagina=1):
    paginacao = Paginator(Servidor.objects.all(), 3)
    try:
        resumo = paginacao.page(pagina)
        # Se a pagina nao for um numero inteiro, pega a primeira
    except PageNotAnInteger:
        resumo = paginacao.page(1)
    except EmptyPage:
        resumo = paginacao.page(paginacao.num_pages)
    return render(request, "index.html", {'servidores': resumo.object_list})
