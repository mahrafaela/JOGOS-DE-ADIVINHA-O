print('********************************')
print('bem vindo ao JOGO DE ADIVINHAÇÃO')
print('********************************')

#definindo o numero secreto
numerosecreto= 16

#definindo o numero de tentativas
numerotentativas= 3

while(numero de tentativas > 0):
    print('ok')

#recebendo o chute do jogador
    chuteString= input('Digite um número')

    print('Você digitou o número', chute)

#declarando as condições
if numerosecreto == chute:
    print('Você acertou!')

elif(chute>numerosecreto):
    print('você errou! O numero secreto é um numero menor')
else: 
    print('você errou! o numero secreto é um numero maior')    