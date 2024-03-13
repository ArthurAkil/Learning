continuar = input('Deseja calcular o IMC de alguem? ')

while continuar == 'sim' or continuar == 'Sim':

    nome = input('\nQual o nome da pessoa? ')

    altura = input('Qual a altura dela? ')
    while not altura.replace('.','',1).isdigit():
        altura = input('Digite apanes numeros para a altura por favor: ')
        while not altura.replace('.','',1).isdigit():
            altura = input('Tente novamente: ')

    peso = input('Qual o peso dela? ')
    while not peso.replace('.','',1).isdigit():
        peso = input('Digite apanes numeros para o peso por favor: ')
        while not peso.replace('.','',1).isdigit():
            peso = input('Tente novamente: ')

    altura_float = float(altura)
    peso_float = float(peso)
    
    imc = peso_float / (altura_float * altura_float)
    
    print(f'A pessoa se chama {nome}, possui {altura_float:.2f} de altura e pesa {peso_float} kilos e seu IMC é {imc:.2f}\n')
    if imc < 18.5:
        print(f'Seu IMC é {imc:.2f}. Você está com magreza.\n')
    elif imc >= 18.6 and imc <= 24.9:
        print(f'Seu IMC é {imc:.2f}. Você está com o peso normal.\n')
    elif imc >= 25 and imc <= 29:
        print(f'Seu IMC é {imc:.2f}. Você está com sobrepeso.\n')
    elif imc >= 30 and imc <= 34.9:
        print(f'Seu IMC é {imc:.2f}. Você está com obesidade grau I.\n')
    elif imc >= 35 and imc <= 39.9:
        print(f'Seu IMC é {imc:.2f}. Você está com obesidade grau II.\n')
    elif imc >= 40:
        print(f'Seu IMC é {imc:.2f}. Você está com obesidade grau III.\n')

    continuar = input('Deseja calcular o IMC de outra pessoa? ')

print('\nPrograma encerrado.')
