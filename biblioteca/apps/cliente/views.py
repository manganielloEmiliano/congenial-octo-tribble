from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def cliente(request):
    doc_externo = loader.get_template('cliente.html')
    ctx = {}
    documento = doc_externo.render(ctx)
    return HttpResponse(documento)
