from django.contrib import admin
from .models import cursos, avaliações

@admin.register(cursos)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo','url', 'criação', 'atualização')

@admin.register(avaliações)
class AvaliaçãoAdmin(admin.ModelAdmin):
    list_display = ('curso','nome','email','avaliação','criação','atualização','ativo')


