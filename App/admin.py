from django.contrib import admin
from models import Servidor, Provedor


# Register your models here.

class AdminServidor(admin.ModelAdmin):
    list_display = ["descricao", "cpu", "ram", "disco"]
    list_editable = ["descricao", "cpu", "ram", "disco"]
    list_filter = ["descricao", "cpu", "ram", "disco"]
    search_fields = ["descricao", "cpu", "ram", "disco"]


class AdminProvedor(admin.ModelAdmin):
    list_display = ["descricao", "logomarca"]
    list_editable = ["descricao"]
    list_filter = ["descricao"]
    search_fields = ["descricao"]


admin.site.register(Servidor, AdminServidor)
admin.site.register(Provedor, AdminProvedor)
