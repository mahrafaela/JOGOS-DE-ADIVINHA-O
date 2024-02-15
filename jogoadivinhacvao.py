print('********************************')
print('bem vindo ao JOGO DE ADIVINHAÇÃO')
print('********************************')

numerosecreto= 16

chute= input('Digite um número')

print('Você digitou o número', chute)

if numerosecreto == chute:
    print('Você acertou!')

else:
    print('Você errou!')
