def scp939():
    entrando = 'Entrando na sala, Você escuta cada vez mais pedidos de socorro, ao se aproximar cada vez mais da vozes.'
    enfrentar = '''Você vê seres estranhos maiores que você e suas cabeças são alongadas, desprovidas de olhos, 
    cada um dos seus quatro membros termina em garras. suas mandíbulas são revestidas de dentes vermelhos. e ultimas 
    coisas que você escuta são eles imitando os gritos de socorro. '''
    saircorrendo = 'você vai embora'
    azar = 'Infelizmente Você não conseguiu sair, pois a porta se fechou'
    sair = choice([saircorrendo, azar])

    cachorro = {
        1: entrando,
        2: enfrentar,
        3: sair
    }

    print('{}'.format(cachorro[1]))
    opcao = str(input('Você quer: \nSe aproxima(1) \nIr embora(2)')).upper()
    if opcao == '2' or opcao == 'EMBORA':
        if sair == saircorrendo:
            print('{}'.format(cachorro[3]))
            return 1
        else:
            print('{}\n{}'.format(cachorro[3], cachorro[2]))
            return 0
    else:
        print('{}'.format(cachorro[2]))
        return 0

# PréAlpha 2.5 BolsonaroEdition