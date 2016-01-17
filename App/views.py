from django.shortcuts import render
from models import Servidor, Provedor


# Create your views here.


def index(request):
    servidores = Servidor.objects.all()
    provedores = Provedor.objects.all()
    return render(request, "index.html", {'servidores': servidores,
                                          'provedores': provedores,
                                          'cpu': get_cpu(),
                                          'ram': get_ram(),
                                          'disco': get_disco()})


def get_cpu():
    list_cpu = list(set([s.cpu for s in Servidor.objects.all()]))
    return list_cpu


def get_ram():
    list_ram = list(set([s.ram for s in Servidor.objects.all()]))
    return list_ram


def get_disco():
    list_disco = list(set([s.disco for s in Servidor.objects.all()]))
    return list_disco
