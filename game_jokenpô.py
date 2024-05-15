def jokenpo():
    from random import randint
    from time import sleep

    lista = ['Pedra', 'Papel', 'Tesoura']
    numero_pc = randint(0, 2)
    escolha_pc = lista[numero_pc]
    vitorias = 0
    derrotas = 0
    empates = 0
    while True:
        print('-'* 70)
        print('Bem vindo ao Jokenpô!')
        print('''Escolha sua opção:
[0] = Pedra
[1] = Papel
[2] = Tesoura
[3] = Sair do jogo''')
        numero_usuario = int(input())
        if numero_usuario == 3:
            return f'Durante o seu tempo de jogo você conseguiu {empates} empates, {vitorias} vitorias, {derrotas} derrotas.'
        elif numero_usuario > 3:
            continue
        escolha_usario = lista[numero_usuario]
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        if numero_usuario == 0:
            print(f'Você escolheu {(lista[numero_usuario]).upper()}', end='')
            if numero_pc == 0:
                print(f' e o computador escolheu {(lista[numero_pc]).upper()}. EMPATE!')
                empates += 1
            elif numero_pc == 1:
                print(f' e o computador escolheu {(lista[numero_pc]).upper()}. O computador ganhou! ')
                derrotas += 1
            elif numero_pc == 2:
                print(f' e o computador escolheu {(lista[numero_pc]).upper()}. Você ganhou!')
                vitorias += 1
        elif numero_usuario == 1:
            print(f'Você escolheu {lista[numero_usuario]}', end='')
            if numero_pc == 0:
                print(f' e o computador escolheu {lista[numero_pc]}. Você ganhou!')
                vitorias += 1
            elif numero_pc == 1:
                print(f' e o computador escolheu {lista[numero_pc]}. EMPATE!')
                empates += 1
            elif numero_pc == 2:
                print(f' e o computador escolheu {lista[numero_pc]}. O computador ganhou!')
                derrotas += 1
        elif numero_usuario == 2:
            print(f'Você escolheu {lista[numero_usuario]}', end='')
            if numero_pc == 0:
                print(f' e o computador escolheu {lista[numero_pc]}. O computador ganhou!')
                derrotas += 1
            elif numero_pc == 1:
                print(f' e o computador escolheu {lista[numero_pc]}. Você ganhou!')
                vitorias += 1
            elif numero_pc == 2:
                print(f' e o computador escolheu {lista[numero_pc]}. EMPATE!')
                empates += 1
