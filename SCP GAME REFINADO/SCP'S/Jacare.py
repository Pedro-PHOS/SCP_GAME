from random import choice

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
scp682()

# PréAlpha 2.5 BolsonaroEdition
