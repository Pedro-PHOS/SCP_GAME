def scp492():

    falas1 = 'Olá meu nome é Jack quem é você? '
    falas2 = 'O-Oi? Estou com medo, você veio para me salvar? Qual é o seu nome? '
    historia1 = 'Antes daqui eu era um boneco de atrações piratas de um parque de diversões '
    historia2 = 'la no parque de diversões que eu morava, eu não fui o unico a ganhar vida, por varias vezes os ' \
                'dinossauros de brinquedo tentaram me devorar '
    Agradecimento = 'Obrigado, de agora em diante serei seu amigo.'
    Comeco = 'Posso te contar um segredo?'
    JackChateado = 'Depois disso Jack nunca mais te respondeu.'
    Saudacoes = choice([falas1, falas2])
    Todos = 'Não tem problema, todos sempre dizem a mesma coisa.'
    historia = choice([historia1, historia2])

    opjack = {
        1: falas1,
        2: falas2,
        3: historia,
        5: Agradecimento,
        6: Comeco,
        7: JackChateado,
        8: Saudacoes,
        9: Todos,
    }

    pessoaJ = input('{}'.format(opjack[8]))
    if pessoaJ == pessoa.nome:
        salvar = input('Obrigado você pode me salvar?\nSalvar Jack:\nSim(S) ou Não(N): ').upper()
        if salvar == 'S' or salvar == 'SIM':
            hist = input('{}'.format(opjack[6]))
            if hist == 'S' or hist == 'SIM':
                print('{}'.format(historia))
            else:
                print('para nao te atrapalhar eu vou ficar quietinho.')
        else:
            print('{}'.format(opjack[9]))
            print('{}'.format(opjack[7]))
    else:
        print('é mentira eu sei o seu nome de verdade, eu posso ser apenas um boneco mas ainda fico chateado quando mentem para mim.')
        print('*{}*'.format(opjack[7]))
    return 1

# PréAlpha 2.5 BolsonaroEdition
