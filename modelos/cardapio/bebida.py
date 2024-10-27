from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco) #herança
        self.tamanho = tamanho

    def __str__(self):
        return self._nome #retornando o nome da bebida
    
    def aplicar_desconto(self):
        self._preco -= round((self._preco * 0.08), 2)