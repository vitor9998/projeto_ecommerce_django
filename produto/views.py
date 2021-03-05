from django.shortcuts import render, redirect, reverse, get_object_or_404   
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from . import models

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 5
class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):

        #return redirect(self.request.META['HTTP_REFERER'])
#Quando o usuário clickar em adicionar ao carrinho, vai fazer o que precisa como
#adicionar mensagem e depois vai volta pra página (HTTP_REFERER, última URL que a pessoa tava)
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
             )
        variacao_id = self.request.GET.get('vid') #segundo get é do dicionário

        if not variacao_id:
            messages.error(
                self.request,
                'Produto não existe'
            )
            return redirect(http_referer)

        variacao = get_object_or_404(models.Variacao, id=variacao_id)

        if not self.request.session.get('carrinho'): #Estou tentando obter a chave carrinho da sessão
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variacao_id in carrinho:
            # TODO: Variação existe no carrinho
            pass
        else:
            # TODO:Variação não existe no carrinho
            pass
#Cookies são arquivos que ficam do lado do cliente que salvam dados úteis
#para aplicação, cookies são únicos para cada pessoa, sessões são tipo cookies mas a
#diferença é que são salvas no lado do servidor (Resumidamente). Por padrão o django
# não salva em um arquivo no servidor, ele vai salvar na base de dados.
        return HttpResponse(f'{variacao.produto} {variacao.nome}')

class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover carrinho')
class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')
class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
