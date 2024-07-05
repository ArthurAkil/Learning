import os
list_products = []
while True:
    product = {}
    switch = input('Selecione uma opção: \n [i]nserir [a]pagar [l]istar [r]esetar [s]air: ')
    if switch.isnumeric():
        print('Você digitou algo além de letras, tenta novamente, por favor.')
    else:
        switch = switch.lower()
        if switch[0] == 'i':
            os.system('cls')
            valor_input = input('Valor: ')
            product[f'{valor_input}'] = int(input('Qual a quantidade: '))
            list_products.append(product)
        elif switch[0] == 'l':
            os.system('cls')
            if len(list_products) == 0:
                print('Nada a listar')
            else:
                for indice in range(len(list_products)):
                    print(f'{indice + 1}º Produto:', end=' ')
                    for keys, values in list_products[indice].items():
                        print(f'{keys}, Quantidade: {values}')
        elif switch[0] == 'a':
            input_indice = input('Qual indice deseja apagar? ')
            if input_indice.isnumeric():
                input_indice = int(input_indice) - 1
                if input_indice <= 0:
                    print('Digite um índice valido da tabela.')
                else:
                    try:
                        del list_products[input_indice] 
                        print(f'Valor da lista na posição {input_indice + 1} foi apagada.')
                    except (ValueError, IndexError):
                        print('Erro desconhecido, tente novamente.')
            else:
                print('Digite um número/índice que deseja apagar, por favor.')
        elif switch[0] == 'r':
            list_products = []
        elif switch[0] == 's':
            break   
        else:
            print('Você não digitou uma letra correspondente ao menu, tente novamente.')