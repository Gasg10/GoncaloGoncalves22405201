from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)

class PT(models.Model):
    nome = models.CharField(max_length=100)

class Sessao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pt = models.ForeignKey(PT, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()