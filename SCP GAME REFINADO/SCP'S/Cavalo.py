def scp042():
    Apresentacao1 = 'Olá, veio fazer experiencia comigo denovo? eu ja não aguento mais!!'
    Apresentacao2 = 'Quem veio me perturbar novamente?'
    Dicas1 = 'existem documentos de todos nós, para voce nao morrer eu indico a voce ler eles.'
    Dicas2 = 'cuidado com aqueles que voce menos desconfia.'
    Dicas = 'você aceita uma dica?'
    CavaloChateado = 'Não tem problema ninguem confiaria em um velho cavalo atrofiado.'
    Saudacoes = choice([Apresentacao1, Apresentacao2])
    EscolhaDicas = choice([Dicas1, Dicas2])
    Adeus = '*você segue em frente, olhando para trás você vê caindo uma lagrima do rosto do cavalo.*'

    cavalo = {
        1: Saudacoes,
        2: EscolhaDicas,
        3: Dicas,
        4: CavaloChateado,
        5: Adeus
    }

    encostar = input('Você vê um Cavalo branco deitado no centro da sala, você quer interagir com ele?'
                     '\nSim(S) ou Não(N):\n').upper()
    if encostar == 'S' or encostar == 'SIM':
        print('{}'.format(cavalo[1]))
        nomec = input('Qual é o seu nome?\n')
        if nomec == pessoa.nome:
            Seg = input('{}\n'.format(cavalo[3])).upper()
            if Seg == 'S' or Seg == 'SIM':
                print('{}\n'.format(cavalo[2]))
            else:
                print('{}\n'.format(cavalo[4]))
        else:
            print('não venha mentir para mim eu sou um cavalo telepata! seu nome é {}.'.format(pessoa.nome))
            print('{}\n'.format(cavalo[5]))
    else:
        print('{}\n'.format(cavalo[5]))

    return 1

# PréAlpha 2.5 BolsonaroEdition
