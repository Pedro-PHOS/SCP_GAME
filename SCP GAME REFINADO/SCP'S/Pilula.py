def scp500():
    fim = 0
    while fim != 1:
        print('Você vê um pequeno pote de plástico com pílulas vermelhas, Você quer tomar?\nSim(S) Não(N)')
        SCP500 = input('Escolha: ').upper()
        if SCP500 in ('S', 'SIM'):
            print('Você toma as pilulas e se sente regenerado.\n')
            print('Você ganhou 1 vida.')
            return 2
        elif SCP500 in ('N', 'NÃO', 'NAO'):
            print('Você não toma as pilulas e vai embora.\n')
            return 1
        else:
            print('\nOpção invalida, Tente novamente.\n')

# PréAlpha 2.5 BolsonaroEdition
