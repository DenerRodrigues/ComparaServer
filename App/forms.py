#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms


class FormServidor(forms.Form):
    descricao = forms.CharField()
    cpu = forms.FloatField()
    ram = forms.CharField()
    disco = forms.CharField()
    so = forms.CharField()
    preco = forms.FloatField()

