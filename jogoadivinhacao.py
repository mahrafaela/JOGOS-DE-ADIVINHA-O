import random;

print('********************************')
print('bem vindo ao JOGO DE ADIVINHAÇÃO')
print('********************************')

#definindo o numero secreto
numerosecreto= round(random.random()*100)
print(numerosecreto)
rodada = 1 
#definindo o numero de tentativas
#numerotentativas= 10

while(rodada <= 3):
    print('tentativas', rodada, 'de', numerotentativas)

#recebendo o chute do jogador
    chuteString= input('Digite um número ente 1 a 100:')
    chute = int(chuteString)

    #print('Você digitou o número', chuteString)
    

#declarando as condições
    if (numerosecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numerosecreto):
        print('você errou! O numero secreto é um numero menor')
    else: 
        print('você errou! o numero secreto é um numero maior')       
    #numerotentativas = numerotentativas - 1    
    rodada = rodada+1   
