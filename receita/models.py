from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.ManyToManyField(Ingrediente)
    favorita_por = models.ManyToManyField(Utilizador, blank=True)