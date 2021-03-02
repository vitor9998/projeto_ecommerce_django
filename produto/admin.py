from django.contrib import admin
from . import models


class VariacaoInLine(admin.TabularInline): #cria uma tabela na parte de baixo na área "Modificar produto" em admin.
    model = models.Variacao
    extra = 1 #exibir um campo extra em branco a mais.

class ProdutoAdmin(admin.ModelAdmin): #Dentro do pruduto quais ilines terão; filhos que você quer editar junto.
    list_display = ['nome','descricao_curta',
               'get_preco_formatado', 'get_preco_promocional_formatado']
    inlines = [
        VariacaoInLine
    ]

admin.site.register(models.Produto, ProdutoAdmin) #para aparecer no admin
admin.site.register(models.Variacao)