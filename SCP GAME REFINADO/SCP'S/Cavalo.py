from random import choice

def scp042():
    fim = 0
    recomeco = 0
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
    while fim != 1:
        encostar = input('Você vê um Cavalo branco deitado no centro da sala, você quer interagir com ele? Sim(S) ou Não(N):\n').upper()
        if encostar in ('S', 'SIM'):
            print('{}'.format(cavalo[1]))
            nomec = input('Qual é o seu nome? ')
            if nomec == pessoa.nome:
                while recomeco != 1:
                    Seg = input('{}\n'.format(cavalo[3])).upper()
                    if Seg in ('S','SIM'):
                        print('{}\n'.format(cavalo[2]))
                        return 1
                    elif Seg in ('N','NAO','NÃO'):
                        print('{}\n'.format(cavalo[4]))
                        return 1
                    else:
                        print('Opção invalida, Tente novamente.')
            else:
                print('não venha mentir para mim eu sou um cavalo telepata! seu nome é {}.'.format(pessoa.nome))
                print('{}\n'.format(cavalo[5]))
        elif encostar in ('N','Não'):
            print('{}\n'.format(cavalo[5]))
            return 1
        else:
            print('Opção invalida, Tente novamente.')

scp042()

# PréAlpha 2.5 BolsonaroEdition
