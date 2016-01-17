from django.shortcuts import render
from models import Servidor, Provedor


# Create your views here.


def index(request):
    return render(request, "index.html", {'servidores': get_servidores(),
                                          'provedores': get_provedores(),
                                          'cpu': get_cpu(),
                                          'ram': get_ram(),
                                          'disco': get_disco()})


def get_servidores():
    servidores = Servidor.objects.all()
    return servidores


def get_provedores():
    return Provedor.objects.all()


def get_cpu():
    return list(set([s.cpu for s in get_servidores()]))


def get_ram():
    return list(set([s.ram for s in get_servidores()]))


def get_disco():
    return list(set([s.disco for s in get_servidores()]))


def form_filtro(request):
    servidores = get_servidores()

    cpu = request.GET['cpu_p']
    disco = request.GET['disco_p']
    ram = request.GET['ram_p']
    provedor = request.GET['provider']

    if cpu:
        servidores = filter(None, [s if str(s.cpu) == cpu else None for s in servidores])

    if disco:
        servidores = filter(None, [s if str(s.disco) == disco else None for s in servidores])

    if ram:
        servidores = filter(None, [s if str(s.ram) == ram else None for s in servidores])

    if provedor:
        servidores = filter(None, [s if str(s.provedor) == provedor else None for s in servidores])

    return render(request, "index.html", {'servidores': servidores,
                                          'provedores': get_provedores(),
                                          'cpu': get_cpu(),
                                          'ram': get_ram(),
                                          'disco': get_disco()})
