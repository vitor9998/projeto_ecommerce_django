#Usei esse arquivo utils para poder reaproveitar essas funções mais de uma vez em meu código,
#evitado repetição
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')