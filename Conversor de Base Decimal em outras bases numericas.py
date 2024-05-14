def converterdecimal(numero_decimal):
    # O código pede um número decimal e dá opções para o usuário escolher em qual base deseja transformar.
    entrada = int(input('Deseja converter o número para qual base? 1- Binário, 2- Octal, 3- Hexadecimal. '))
    #Criada lista vazia para armazenar os valores das divisões durante a transformação
    lista = []
    if entrada == 1:
        # Criado um loop para que seja feita uma divisão inteira para que o código não divida infinamente numeros quebrados
        # E ao final seja adicionado o valor 'resto' das divisões na lista
        while numero_decimal != 0:
            num = numero_decimal % 2
            numero_decimal //= 2
            lista.append(num)
        return lista[::-1]
    elif entrada == 2:
        while numero_decimal != 0:
            num = numero_decimal % 8
            numero_decimal //= 8
            lista.append(num)
        # Retornei a lista ao contrário pois se lê os restos das divisões de maneira inversa
        return lista[::-1]
    elif entrada == 3:
        while numero_decimal != 0:
            num = numero_decimal % 16
            numero_decimal //= 16
            lista.append(num)
        # Aqui foi criado um algoritmo que vai substituir os valores da lista de 10 a 15 pelas letras, especialidade da conversão para base hexadecimal
        if 10 in lista:
            # Adiconei a respectiva letra ao numero e utilizei o 'index(x)' para saber em qual indice ele estaria 
            # Fazendo com que seja o indice em que estava 10 vá +1 para frente e o 'A' fique em seu lugar
            lista.insert(lista.index(10), 'A')
            # Após isso retirei o valor 10 da lista pois já teria sido substituido pelo 'A' e usei a mesma logica do 'index(x)' para servir
            # como indice, fazendo com que vá direto ao indice que está localizado o 10
            lista.pop(lista.index(10))
        if 11 in lista:
            lista.insert(lista.index(11), 'B')
            lista.pop(lista.index(11))
        if 12 in lista:
            lista.insert(lista.index(12, 'C'))
            lista.pop(lista.index(12))
        if 13 in lista:
            lista.insert(lista.index(13), 'D')
            lista.pop(lista.index(13))
        if 14 in lista:
            lista.insert(lista.index(14), 'E')
            lista.pop(lista.index(14))
        if 15 in lista:
            lista.insert(lista.index(15), 'F')
            lista.pop(lista.index(15))
        return lista[::-1]
