while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+, -, /, *, ^): ')

    numero_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+, -, /, *, ^'

    if operador not in operadores_permitidos:
        print('Operador inválido.')

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'A soma do {num1_float} + {num2_float} = {num1_float + num2_float}')
    elif operador == '-':
        print(f'A subtração do {num1_float} - {num2_float} = {num1_float - num2_float}')
    elif operador == '/':
        print(f'A divisão do {num1_float} / {num2_float} = {num1_float / num2_float}')
    elif operador == '*':
        print(f'A multiplicação do {num1_float} * {num2_float} = {num1_float * num2_float}')
    elif operador == '^':
        print(f'A exponenciação do {num1_float} ^ {num2_float} = {num1_float ** num2_float}')
    else:
        print('Nunca deveria chegar aqui.')


    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
