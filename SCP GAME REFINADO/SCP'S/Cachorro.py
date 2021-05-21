def scp939():
    entrando = 'Entrando na sala, Você escuta cada vez mais pedidos de socorro.'
    enfrentar = '''Você vê seres estranhos maiores que você e suas cabeças são alongadas, desprovidas de olhos, 
cada um dos seus quatro membros termina em garras. suas mandíbulas são revestidas de dentes vermelhos.
As ultimas coisas que você escuta antes de ser devorado. são eles imitando os gritos de socorro das suas antigas vitimas.'''
    saircorrendo = 'você encontra a porta no meio da escuridão, e vai embora.'
    azar = 'Infelizmente Você não conseguiu sair, pois estava muito escuro.'
    sair = choice([saircorrendo, azar])

    cachorro = {
        1: entrando,
        2: enfrentar,
        3: sair
    }

    print('{}'.format(cachorro[1]))
    print('A sala e muito grande e escura, você não enxerga quase nada a sua frente, porem escuta gritos ecoando pela sala.')
    opcao = str(input('Você quer: \nProcurar os pedidos de socorro(1) \nTentar achar a proxima porta na escuridão(2):\n')).upper()
    if opcao == '2' or opcao == 'PORTA':
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