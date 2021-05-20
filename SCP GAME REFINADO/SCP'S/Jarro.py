def scp019():
    entrando = 'Você vê no centro da sala uma jarra de cerâmica, com uma boca de 1,8 m de diâmetro e 2,4 m de altura.'
    enfrentar = 'Você se aproxima da jarra'
    saircorrendo = 'você vai embora'
    azar = 'Infelizmente Você não conseguiu sair, pois a porta se fechou'
    sair = choice([saircorrendo, azar])
    devorado = 'de dentro da jarra saem criaturas do tamanho de pugs e te devoram vivo.'

    jarro = {
        1: entrando,
        2: enfrentar,
        3: sair,
        4: devorado
    }

    print('{}'.format(jarro[1]))
    opcao = str(input('Você quer: \nSe aproxima(1) ou Ir embora(2)\n')).upper()
    if opcao == '2' or opcao == 'EMBORA':
        if sair == saircorrendo:
            print('{}'.format(jarro[3]))
            return 1
        else:
            print('{}\n{}'.format(jarro[3], jarro[4]))
            return 0
    else:
        print('{}{}'.format(jarro[2], jarro[4]))
        return 0

# PréAlpha 2.5 BolsonaroEdition
