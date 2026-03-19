from django.contrib import admin
from .models import Ingrediente, Utilizador, Receita

admin.site.register(Ingrediente)
admin.site.register(Utilizador)
admin.site.register(Receita)