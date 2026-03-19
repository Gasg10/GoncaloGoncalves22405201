from django.contrib import admin
from .models import Quizz, Pergunta, Resposta

admin.site.register(Quizz)
admin.site.register(Pergunta)
admin.site.register(Resposta)