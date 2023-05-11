from django.db import models

# Create your models here.



class Moeda(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)
    alto = models.FloatField()
    baixo = models.FloatField()
    compra = models.FloatField()
    venda = models.FloatField()
    data_atualizacao = models.CharField(max_length=20)
    favoritada = models.BooleanField(default=False)
    comparacao = models.BooleanField(default=False)