print('********************************')
print('bem vindo ao JOGO DE ADIVINHAÇÃO')
print('********************************')

#definindo o numero secreto
numerosecreto= 16
rodada = 1 
#definindo o numero de tentativas
numerotentativas= 3

while(rodada <= 3):
    print('tentativas ', rodada, 'de', numerotentativas)

#recebendo o chute do jogador
    chuteString= input('Digite um número')

    #print('Você digitou o número', chuteString)
    chute = int(chuteString)

#declarando as condições
    if (numerosecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numerosecreto):
        print('você errou! O numero secreto é um numero menor')
    else: 
        print('você errou! o numero secreto é um numero maior') 
    rodada = rodada+1       
    #numerotentativas = numerotentativas - 1    

