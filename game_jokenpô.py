def jokenpô():
    from random import choice

    pedra = 'pedra'
    papel = 'papel'
    tesoura = 'tesoura'
    vitorias = 0
    derrotas = 0
    while True:
        print('Deseja jogar ou continuar jogando Jokenpô? 1-Sim 2-Não')
        mediador = int(input())
        adversario = ''
        if mediador == 1:
            entrada = input('Faça uma escolhe entre Pedra, Papel ou Tesoura: ').lower()
            adversario = choice([pedra, papel, tesoura])
            if entrada == 'pedra' and adversario == papel:
                print(f'Você escolheu {entrada} e o adversário escolheu {adversario}. Você perdeu.')
                derrotas += 1
            elif entrada == 'pedra' and adversario == tesoura:
                print(f'Você escolheu {entrada} e o adversário escolheu {adversario}. Você ganhou.')
                vitorias += 1
            elif entrada == 'pedra' and adversario == pedra:
                print(f'Você escolheu {entrada} e o adversário escolheu {adversario}. Empate.')

            elif entrada == 'papel' and adversario == tesoura:
                print(f'Você escolheu {entrada} e o adversário escolheu {adversario}. Você perdeu.')
                derrotas += 1
            elif entrada == 'papel' and adversario == pedra:
                print(f'Você escolheu {entrada} e o adversário escolheu {adversario}. Você ganhou.')
                vitorias += 1
            elif entrada == 'papel' and adversario == papel:
                print(f'Você escolheu {entrada} e o adversário escolheu {adversario}. Empate.')

            elif entrada == 'tesoura' and adversario == tesoura:
                print(f'Você escolheu {entrada} e o adversário escolheu {adversario}. Empate.')
            elif entrada == 'tesoura' and adversario == pedra:
                print(f'Você escolheu {entrada} e o adversário escolheu {adversario}. Você perdeu.')
                derrotas += 1
            elif entrada == 'tesoura' and adversario == papel:
                print(f'Você escolheu {entrada} e o adversário escolheu {adversario}. Você ganhou.')
                vitorias += 1
        elif mediador == 2:
            return f'A contagem de suas vitorias contra o computador foram {vitorias} e suas derrotas foram {derrotas}.'
        else:
            print(f'Você não digitou uma opção válida.')
