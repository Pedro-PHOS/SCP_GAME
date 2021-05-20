def scp500():
    SCP500 = input(
        'Você vê um pequeno pote de plástico com pílulas vermelhas, Você quer tomar? \nSim(S) Não(N)\n').upper()
    if SCP500 == 'S' or SCP500 == 'SIM':
        print('Você toma as pilulas e se sente regenerado.\n')
        print('Você ganhou 1 vida.')
        return 2
    else:
        print('Você não toma as pilulas e vai embora.\n')
        return 1

# PréAlpha 2.5 BolsonaroEdition
