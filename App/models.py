from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Provedor(models.Model):
    descricao = models.CharField(max_length=120, verbose_name="Descricao", null=False)
    logomarca = models.ImageField(verbose_name="Logomarca", null=True, blank=True)

    def __unicode__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Provedores"


class Servidor(models.Model):
    descricao = models.CharField(max_length=120, verbose_name="Descricao", null=False)
    cpu = models.IntegerField(verbose_name="Cpu")
    ram = models.IntegerField(verbose_name="Ram/Gb")
    disco = models.IntegerField(verbose_name="Disco/Gb")
    so = models.CharField(max_length=60, verbose_name="Sistema Operacional")
    preco = models.FloatField(verbose_name="Preco/Mes")
    provedor = models.ForeignKey(Provedor, verbose_name="Provedor")

    def __unicode__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Servidores"
