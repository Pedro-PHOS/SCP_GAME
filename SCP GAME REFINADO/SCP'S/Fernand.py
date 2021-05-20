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
    'Napoleão', 'O Hulk', 'Alexandre o Grande', 'Capitão Gancho', 'Sherlock Holmes', 'Dr. Frankenstein',
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

# PréAlpha 2.5 BolsonaroEdition
