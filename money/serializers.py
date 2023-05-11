from rest_framework import serializers
from .models import Moeda


class MoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moeda
        fields = ['id', 'nome', 'sigla', 'alto', 'baixo', 'compra', 'venda', 'data_atualizacao', 'favoritada', 'comparacao']