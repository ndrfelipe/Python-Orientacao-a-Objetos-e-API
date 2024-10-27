from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet') #Criando um restaurante

bebida_suco = Bebida("Suco de Melancia", 8.0, "grande") #cadastrando um suco no restaurante
bebida_suco.aplicar_desconto() #aplicandp desconto no suco

prato_hamburguer = Prato("Hamburguer do Chef", 24.99, 'Pão com gergelim, carne e bacon') # cadastrando um prato no restaurante
prato_hamburguer.aplicar_desconto() #aplicando desconto no prato

coxinha = Prato("Coxinha", 7.5, 'Coxinha de grango') # cadastrando um prato no restaurante

sorvete = Sobremesa("Sorvete tropical", 4.99, "Sorvete de Limão")

#adicionando os pratos no cardápio do restaurante praça
restaurante_praca.adicionar_no_cardapio(bebida_suco) 
restaurante_praca.adicionar_no_cardapio(prato_hamburguer)
restaurante_praca.adicionar_no_cardapio(coxinha)
restaurante_praca.adicionar_no_cardapio(sorvete)



def main():
    #exibindo o cardápio do restaurante praça.
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()