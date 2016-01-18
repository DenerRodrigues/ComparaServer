from django.shortcuts import render
from models import Servidor, Provedor


# Create your views here.


def index(request):
    return render(request, "index.html", {'servidores': get_servidores(),
                                          'provedores': get_provedores(),
                                          'cpu': get_cpu(),
                                          'ram': get_ram(),
                                          'disco': get_disco(),
                                          'order_price': '1'})


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

    preco = request.GET['filter_price']
    cpu = request.GET['cpu_p']
    disco = request.GET['disco_p']
    ram = request.GET['ram_p']
    provedor = request.GET['provider']

    if preco:
        servidores = filter(None, [
            s if float(str(s.preco)) <= float(str(preco).replace(',', '.')) else None for s in
            servidores])

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
                                          'disco': get_disco(),
                                          'order_price': '1'})


def form_order(request):
    servidores = get_servidores()
    servidores = servidores.order_by("preco")

    order = request.GET['order_price'] or '1'

    if order == '1':
        order = '2'
    elif order == '2':
        order = '1'
        servidores = servidores.reverse()

    return render(request, "index.html", {'servidores': servidores,
                                          'provedores': get_provedores(),
                                          'cpu': get_cpu(),
                                          'ram': get_ram(),
                                          'disco': get_disco(),
                                          'order_price': order})
