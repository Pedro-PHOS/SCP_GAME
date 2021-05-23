from random import choice

def scp019():
    fim = 0
    entrando = 'Você vê no centro da sala um jarro de cerâmica, com mais de 2 metros!'
    enfrentar = 'Você se aproxima do jarro'
    saircorrendo = 'você vai embora'
    azar = 'Infelizmente Você não conseguiu sair, pois a porta se fechou'
    sair = choice([saircorrendo, azar])
    devorado = 'de dentro do jarro saem criaturas do tamanho de pugs e te devoram vivo'

    jarro = {
        1: entrando,
        2: enfrentar,
        3: sair,
        4: devorado
    }
    print('{}'.format(jarro[1]))
    while fim != 1:
        opcao = str(input('Você quer, (1)Se aproxima ou (2)Ir embora.\nOpção: ')).upper()
        if opcao in ('2', 'EMBORA', 'IR EMBORA', 'SAIR'):
            if sair == saircorrendo:
                print('{}.'.format(jarro[3]))
                return 1
            else:
                print('{}.\n{}.'.format(jarro[3], jarro[4]))
                return 0
        elif opcao in ('1', 'APROXIMAR'):
            print('{}, {}.'.format(jarro[2], jarro[4]))
            return 0
        else:
            print('Opção invalida, Tente novamente.')
scp019()

# PréAlpha 2.5 BolsonaroEdition
