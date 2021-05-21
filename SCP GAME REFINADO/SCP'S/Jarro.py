def scp019():
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
    opcao = str(input('Você quer: \nSe aproxima(1) ou Ir embora(2):\n')).upper()
    if opcao == '2' or opcao == 'EMBORA':
        if sair == saircorrendo:
            print('{}.'.format(jarro[3]))
            return 1
        else:
            print('{}.\n{}.'.format(jarro[3], jarro[4]))
            return 0
    else:
        print('{}, {}.'.format(jarro[2], jarro[4]))
        return 0

# PréAlpha 2.5 BolsonaroEdition
