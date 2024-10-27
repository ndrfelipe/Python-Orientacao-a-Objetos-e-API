from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #conceito de herança
        self.descricao = descricao
    
    def __str__(self):
        return self._nome #retornando o valor de nome
    
    def aplicar_desconto(self): #conceito de classe abstrata 
        """ 
        classe abstrata vinda da classe ItemCardapio.  
        Polimorfismo, o mesmo método vai se comportar de forma diferente em classes diferentes.
        
        """
        self._preco -= round((self._preco * 0.05), 2)