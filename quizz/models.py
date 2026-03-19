from django.db import models

class Quizz(models.Model):
    titulo = models.CharField(max_length=100)

class Pergunta(models.Model):
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)