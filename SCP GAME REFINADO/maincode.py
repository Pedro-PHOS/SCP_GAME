# anotaçoes: acrescentar mais na jogabilidade e historia, mais scps, e um metodo que depois de uma quantidade de loops
# o game acaba

from time import sleep
from random import choice  # Biblioteca Random


# import pygame
# pygame.init()
# pygame.mixer.music.load('betasom.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()


def progress_bar(done):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100), end='')

def carregando():
    for n in range(6):
        progress_bar(n / 5)
        sleep(1)


# =================================================== FUNÇÕES ====================================================== #

# === SCP-019 === Jarro

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

# === SCP-500 === Pilulas

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


# === SCP-682 === Jacare

def scp682():
    fim = 0
    entrando = '''A porta da sala se fecha.\nO reptil esta no centro da sala.'''
    enfrentar = '''O reptil que estava no centro da sala vai em sua direção e com a suas garras e mandibula ele te 
agarra, Antes dele te dilacerar você tem um pensamento como se você sentisse a dor e traumas que ele passou aqui.'''
    saircorrendo = 'você sai correndo em direção a porta'
    azar = 'Infelizmente Você não conseguiu correr, pois ele foi mais rapido!'
    sair = choice([saircorrendo, azar])

    jacare = {
        1: entrando,
        2: enfrentar,
        3: sair,
    }
    print('{}'.format(jacare[1]))
    while fim != 1:
        opcao = str(input('Você quer, (1)Enfrentar ou (2)Sair correndo.\nOpção: ')).upper()
        if opcao in ('2', 'CORRER'):
            if sair == saircorrendo:
                print('{}.'.format(jacare[3]))
                return 1
            else:
                print('{}\n{}'.format(jacare[3], jacare[2]))
                return 0
        elif opcao in ('1', 'ENFRENTAR'):
            print('{}'.format(jacare[2]))
            return 0
        else:
            print('Opção Invalida, Tente novamente.')


# == SCP-492 === Jack

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


# === SCP-939 ==== Cachorro

def scp939():
    fim = 0
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
    print('A sala é muito grande e escura, você não enxerga quase nada a sua frente, porem escuta gritos ecoando pela sala.')

    while fim != 1:
        print('Você quer: \n(1)Procurar os pedidos de socorro.\n(2)Tentar achar a proxima porta na escuridão.')
        opcao = input('Escolha: ').upper()
        if opcao in ('2','PORTA'):
            if sair == saircorrendo:
                print('{}'.format(cachorro[3]))
                return 1
            else:
                print('{}\n{}'.format(cachorro[3], cachorro[2]))
                return 0
        elif opcao in ('1','PROCURAR',):
            print('{}'.format(cachorro[2]))
            return 0
        else:
            print('Opção invalida, tente novamente.')


# === SCP-042 === Cavalo

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


# === SCP-042 === Fernand

def pensando_1(done):
    print("\r{0:10s}".format('.' * int(done * 1), done * 1), end='')


def persando():
    for n in range(9):
        pensando_1(n / 1)
        sleep(0.5)


def scp085():
    apresentacao = 'Olá quem vós fala é o vigésimo segundo rei da frança, Fernand primeiro!'
    charadas = choice(['Nem tudo que reluz é ouro.', 'O Inferno está vazio e todos os demônios estão aqui.',
                       'É mais fácil obter o que se deseja com um sorriso do que à ponta da espada.'])
    mentiras = choice(['Uma camponesa da Inglaterra', 'Um vampiro', 'Um homúnculo', 'Garibaldo', 'André o Gigante'
                                                                                                 'Napoleão', 'O Hulk',
                       'Alexandre o Grande', 'Capitão Gancho', 'Sherlock Holmes', 'Dr. Frankenstein',
                       'O monstro de Frankenstein'])

    fernand = {
        1: apresentacao,
        2: charadas,
        3: mentiras
    }

    print('{}\n'.format(fernand[1]))
    ajoelhar = input('não vai se ajoelhar? \nSim(S) Não(N)\n').upper()
    if ajoelhar == 'S' or ajoelhar == 'SIM':
        print('enquanto vc se ajoelhava Fernand devorou sua cabeça.')
        return 0
    else:
        print('mas que audacia não se ajoelhar perante a mim, mas dessa vez eu vou deixar passar.')
        sleep(2)
        print('\n*Fernand puxa uma cadeira e te obriga a sentar* \n *Ele te serve uma xicara de chá*')
        sleep(3)
        print('\nninguem me visita faz horas eu estava ficando preocupado, o que você deseja?')
        desejo = input('(1)ir embora (2)Ficar e tomar um chá\n ')
        if desejo == '1':
            print('Eu até posso de deixar ir embora, mas ai eu vou ficar sozinho, porem como eu sou um cavalheiro,'
                  ' se você acertar minha charada eu deixo vc ir.')
            sleep(3)
            charadas2 = input('Qual dessas frases é de William Shakespeare. \n'
                              '(1) Ser feliz sem motivo é a mais autêntica forma de felicidade.\n(2){} \n'
                              '(3)A esperança é o sonho do homem acordado.\n'.format(fernand[2]))
            if charadas2 == '2':
                print('\nVocê acertou pode ir embora, a porta esta atrás das cortinas rosas.')
                return 1
            else:
                print('você errou!, Fernand devora sua cabeça.')
                return 0
        elif desejo == '2':
            print('*Algums momentos depois*')
            sleep(2)
            print('bem como você ficou aqui e tomou um chá comigo eu te dou o direito de 1 pergunta.')
            sleep(2)
            pergunta = input('O que você quer saber?\n(1)Como sair daqui \n(2)Como você veio parar aqui?'
                             '\n(3)Você realmente é o rei da frança?\n')
            if pergunta == '1':
                print('isso é facil, como você é um visitante e só passar pela porta atras das cortinas rosas.')
                print('Afinal aqui é meu castelo, e por isso não posso sair.')
                return 1
            elif pergunta == '2':
                print('Antigamente eu era, {}, porem eu fui mordido por um elefante radiotivo e vim parar aqui.'.format(
                    fernand[3]))
                print('Como eu ja respondi sua pergunta pode ir embora, so passar pela porta atras das cortinas rosas')
                return 1
            elif pergunta == '3':
                persando()
                print('\n\n*Fernand devorou sua cabeça*.')
                return 0


# ============================================ DICIONARIO DE OPÇÕES ================================================== #

escolha1 = "Você vê uma grande jarra de cerâmica no centro da sala."
escolha2 = 'Você vê um pequeno pote em cima de uma mesa.'
escolha3 = 'Você vê uma grande criatura vagamente semelhante a um réptil.'
escolha4 = 'Você vê um pequeno boneco pirata de pano sentado no canto da sala.'
escolha5 = 'Você encontra uma sala escura, nao consegue enchergar o que esta dentro, porem escuta pedidos de socorro!'
escolha6 = 'Você vê um cavalo branco deitado no centro da sala.'
escolha7 = 'Você vê um grande quarto decorado no estilo palacio da realeza françesa.'

option = {
    1: escolha1,
    2: escolha2,
    3: escolha3,
    4: escolha4,
    5: escolha5,
    6: escolha6,
    7: escolha7,
}

number_of_scp = int(len(option))


def escolhesala(num):
    if num == 1:
        return scp019()
    elif num == 2:
        return scp500()
    elif num == 3:
        return scp682()
    elif num == 4:
        return scp492()
    elif num == 5:
        return scp939()
    elif num == 6:
        return scp042()
    elif num == 7:
        return scp085()
    else:
        return -1


# ================================================= Personagem ======================================================= #

class Personagem:
    def __init__(self):
        self.nome = []
        self.vida = 3
        self.pontos = 5


# ================================================ Codigo Salas ====================================================== #


def remove_option(lista, n):  # função para tirar salas ja utilizadas
    contador = 0
    while contador < number_of_scp:
        if lista[contador] == n:
            lista[contador] = 0
        contador += 1


def proceduresala(vida, op):  # Função para calcular a vida

    if vida == 1:
        print("Última vida.. que a sorte esteja com você!")
        sleep(3)
    elif vida == 2:
        print("Tome cuidado: lhe restam apenas 2 vidas.")
        sleep(3)
    elif vida >= 4:
        print("Por sorte você tem {} vidas e {} a extra! \nTotal de vidas = {}".format('3', vida - 3, vida))
        sleep(3)

    # ============================================== Codigo Game ==================================================== #
   
    print('\nAgora Você tem no total [{}]Pontos'.format(ponto.pontos))
    print('\nVocê está em um corredor e existem duas portas, uma na direita e outra na esquerda.')  # Narração Basica
    sleep(2)

    esquerda = choice(op)  # Programa para escolher  os SCP
    direita = choice(op)
    while esquerda == direita or esquerda == 0 or direita == 0:
        esquerda = choice(op)
        direita = choice(op)

    sala = input("\nEscolha: direita [D] ou esquerda [E]\n").upper()  # Programa pata entrar nas salas
    if sala == 'D' or sala == 'DIREITA':
        print('Você entra na sala da Direita e olha pela porta.\n')
        sleep(2)
        print("{}\n".format(option[direita]))

        Entrar = input('Voce quer entrar ? Sim(S) Não(N)\n').upper()
        if Entrar == 'S' or sala == 'SIM':
            remove_option(op, direita)
            x = escolhesala(direita)
            if x == 0:
                print("\nVocê morreu, Escolha melhor da próxima vez.\n")
                sleep(3)
                vida -= 1
                ponto.pontos -= 1
            elif x == 1 or x == 2:
                if x == 2:
                    vida += 1
                print("\nParabéns, Você conseguiu passar pela sala.\n")
            sleep(3)
        else:
            print('Como você não entrou na sala da direita, então Automaticamente você foi para a da esquerda.\n')
            sleep(5)
            remove_option(op, esquerda)
            x = escolhesala(esquerda)
            if x == 0:
                print("\nVocê morreu, Escolha melhor da próxima vez.\n")
                sleep(3)
                vida -= 1
                ponto.pontos -= 1
            elif x == 1 or x == 2:
                if x == 2:
                    vida += 1
                print("\nParabéns, Você conseguiu passar pela sala.\n")
            sleep(3)

    elif sala == 'E' or sala == 'ESQUERDA':
        print('Você entra na sala da Esquerda e olha pela porta\n.')
        sleep(2)
        print("{}\n".format(option[esquerda]))
        sleep(3)
        Entrar = input('Voce quer entrar ? Sim(S) Não(N)\n').upper()
        if Entrar == 'S' or Entrar == 'SIM':
            remove_option(op, esquerda)
            x = escolhesala(esquerda)
            if x == 0:
                print("\nVocê morreu. Escolha melhor da próxima vez.\n")
                vida -= 1
                ponto.pontos -= 1
            elif x == 1 or x == 2:
                if x == 2:
                    vida += 1
                print("\nParabéns. Você conseguiu passar pela sala.\n")
            sleep(3)

        else:
            print('Como você não entrou na sala da Esquerda, então Automaticamente você foi para a da direita. \n')
            remove_option(op, direita)
            x = escolhesala(direita)
            if x == 0:
                print("\nVocê morreu. Escolha melhor da próxima vez.\n")
                vida -= 1
                ponto.pontos -= 1
            elif x == 1 or x == 2:
                if x == 2:
                    vida += 1
                print("\nParabéns. Você conseguiu passar pela sala.\n")
            sleep(3)
    else:
        print('Essa opção não e valida')
    if vida > 0:
        proceduresala(vida, op)


options = []
i = 0

while i < number_of_scp:
    i += 1
    options.append(i)

left = choice(options)
right = choice(options)
ponto = Personagem()

print('\n=== Hola Bem Vindo ao mundo de SCP ===\n')
print('''Isso é uma simulação para preparar os novatos da fundação em caso de emergencia!
Regras:
1º Tudo que acontecer neste simulado não podera ser divulgado a nimguem!
2º As opções estarão em''', 'Verde'),('Vermelho! ou dentro de ().')
print('3º Tudo que for para inserir uma resposta estara em Azul.')
sleep(2)
pessoa = Personagem()
pessoa.nome = input("Digite seu nome para começarmos:\n")
carregando()
print('\nPrazer em te conhecer Sr(a) {}.\n'.format(pessoa.nome))
print("Sempre que você passar por uma sala, seja vivo ou morto, você voltará nesse ponto.\nNão se esqueça: "
      "você tem APENAS 3 vidas!")
sleep(5)

proceduresala(pessoa.vida, options)

# PréAlpha 2.5 BolsonaroEdition
