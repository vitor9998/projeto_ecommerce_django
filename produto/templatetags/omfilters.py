#arquivo criado inicialmente para criação de um filtro para aparecer os numeros do ecommerce como dinheiro.
#onde vou criar todos os meus filtros necessários.
from django.template import Library
from utils import utils

register = Library()

@register.filter
def formata_preco(val):
    return utils.formata_preco(val)