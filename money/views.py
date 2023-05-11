from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from .models import Moeda
from .serializers import MoedaSerializer
import datetime
from django.db.models import Q

# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI

@api_view(['POST'])
def setConfig(request):
    dataMoeda = request.data
    sigla = dataMoeda['sigla']
    try:
        moeda = Moeda.objects.get(sigla=sigla)
    except Moeda.DoesNotExist:
        raise Http404()
    
    if request.path == '/api/fav/':
        moeda.favoritada = not moeda.favoritada
    elif request.path == '/api/comp/':
        Moeda.objects.exclude(Q(id=moeda.id)).update(comparacao=False)
        moeda.comparacao = not moeda.comparacao
    moeda.save()

    serialized_moeda = MoedaSerializer(moeda)
    return Response(serialized_moeda.data)


@api_view(['GET'])
def getCotacao(request, moedas):
    url = f"https://economia.awesomeapi.com.br/last/{moedas}"
    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        raise Http404(str(err))
    
    data = response.json()
    for moeda in data:
        try:
            moeda_obj = Moeda.objects.get(sigla=data[moeda]['code'])
        except Moeda.DoesNotExist:
            moeda_obj = Moeda(
                sigla=data[moeda]['code'],
                nome=data[moeda]['name'],
                alto=data[moeda]['high'],
                baixo=data[moeda]['low'],
                compra=data[moeda]['bid'],
                venda=data[moeda]['ask'],
                data_atualizacao=data[moeda]['create_date'],
                favoritada=False,
                comparacao=False
            )
            moeda_obj.save()
        else:
            moeda_obj.alto = data[moeda]['high']
            moeda_obj.baixo = data[moeda]['low']
            moeda_obj.compra = data[moeda]['bid']
            moeda_obj.venda = data[moeda]['ask']
            moeda_obj.data_atualizacao = data[moeda]['create_date']
            moeda_obj.save()
    
    return Response(data)

def getFav(request):
    moedas = Moeda.objects.filter(favoritada=True)
    serialized_moedas = [moeda.sigla for moeda in moedas]
    return JsonResponse({'moedas': serialized_moedas})

def getComp(request):
    moedas = Moeda.objects.filter(comparacao=True)
    serialized_moedas = moedas[0].sigla
    return JsonResponse({'comparacao': serialized_moedas})

def api_moeda(request, nome):
    try:
        moeda = Moeda.objects.get(nome=nome)
    except Moeda.DoesNotExist:
        raise Http404()
    serialized_moeda = MoedaSerializer(moeda)
    return Response(serialized_moeda.data)

