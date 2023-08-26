from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def libros(request):
    doc_externo = loader.get_template('libro.html')
    ctx={}
    documento = doc_externo.render(ctx)
    return HttpResponse(documento)
