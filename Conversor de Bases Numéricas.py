#criei uma função que mostra os numeros formatados fora da lista
def mostrar_formatado(numero):
    return ''.join(str(i) for i in numero)

def converterdecimal(numero_decimal):
    # O código pede um número decimal e dá opções para o usuário escolher em qual base deseja transformar.
    entrada = int(input('Deseja converter o número decimal para alguma base? 1-Binário, 2-Octal, 3-Hexadecimal, 4-Encerrar programa: '))
    #Criada lista vazia para armazenar os valores das divisões durante a transformação
    lista = []
    if entrada == 1:
        # Criado um loop para que seja feita uma divisão inteira para que o código não divida infinamente numeros quebrados
        # E ao final seja adicionado o valor 'resto' das divisões na lista
        while numero_decimal != 0:
            num = numero_decimal % 2
            numero_decimal //= 2
            lista.append(num)
        #ajustei a lista para que ela fique com o valor certo de trás para frente, armazenei caso precise futuramente para algo
        lista = lista[::-1]
        #posso converter esse convertido em int qnd for em binario e octal, agora em hexa precisa ser str pois tem letras no hexa
        convertido = mostrar_formatado(lista)
        return convertido
    elif entrada == 2:
        while numero_decimal != 0:
            num = numero_decimal % 8
            numero_decimal //= 8
            lista.append(num)
        lista = lista[::-1]
        #variavel que irá receber os valores da lista em forma de str e retorno dessa variavel
        convertido = mostrar_formatado(lista)
        return convertido
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
        lista = lista[::-1]
        convertido = mostrar_formatado(lista)
        return convertido
    else:
        return f'Programa encerrado'

def converterbinario(entrada_bin):
    #transformei o valor de entrada em string para poder passar ele para manusear ele e colocalo dentro de uma lista
    entrada_bin = str(entrada_bin)
    lista = []
    #for para percorrer a entrada(str) e transformar cada valor em int e adiciona-los na lista
    for i in entrada_bin:
        i = int(i)
        lista.append(i)
    #lista nova criada que irá armazenar a resposta
    resposta = []
    resultado = 0
    aux = len(lista) - 1
    #for para percorrer os valores da lista e soma-los, colocando o valor final na lista (resposta), diminuindo o aux (auxiliar) que quando chegar a 0 o for encerra
    for i in lista:
        num_decimal = i * (2 ** aux)
        resultado += num_decimal
        aux -= 1
        if aux < 0:
            resposta.append(resultado)
            break
    #transformei o resultado que ficou armazenado na lista resposta[0] em uma variavel para poder transforma-lo em outra base
    numero_decimal = resposta[0]
    print(f'Seu valor de base binario {entrada_bin} vale {numero_decimal} na base decimal.')
    return converterdecimal(numero_decimal)

def converteroctal(entrada_octal):
    #transformei o valor de entrada em string para poder passar ele para manusear ele e colocalo dentro de uma lista
    entrada_octal = str(entrada_octal)
    lista = []
    #for para percorrer a entrada(str) e transformar cada valor em int e adiciona-los na lista
    for i in entrada_octal:
        i = int(i)
        lista.append(i)
    #lista nova criada que irá armazenar a resposta
    resposta = []
    resultado = 0
    aux = len(lista) - 1
    #for para percorrer os valores da lista e soma-los, colocando o valor final na lista (resposta), diminuindo o aux (auxiliar) que quando chegar a 0 o for encerra
    for i in lista:
        num_decimal = i * (8 ** aux)
        resultado += num_decimal
        aux -= 1
        if aux < 0:
            resposta.append(resultado)
            break
    #transformei o resultado que ficou armazenado na lista resposta[0] em uma variavel para poder transforma-lo em outra base
    numero_decimal = resposta[0]
    print(f'Seu valor de base octal {entrada_octal} vale {numero_decimal} na base decimal.')
    return converterdecimal(numero_decimal)

def converterhexa(entrada_hexa):
    # A função só funciona se a entrada for em string (ex.: 0f), pois se colocar em int vai dar erro pois f é string
    #peguei o valor de entrada e o transformei em maiusculo e por via das dúvidas ainda o transformei em str de novo
    entrada_hexa = str(entrada_hexa).upper()
    lista = []
    #indicador para guardar o valor de cada letra da base hexadecimal
    indicador = 0
    #for para percorrer a entrada(str) e transformar cada valor str em um valor com uma variavel pegando seu valor
    #e verificando se o numero já estiver em str e for int ele apenas transforma e adiciona a lista 
    for i in entrada_hexa:
        if i == 'A':
            i = 10
        if i == 'B':
            i = 11
        if i == 'C':
            i = 12
        if i == 'D':
            i = 13
        if i == 'E':
            i = 14
        if i == 'F':
            i = 15
        i = int(i)
        lista.append(i)
    #lista nova criada que irá armazenar a resposta
    resposta = []
    resultado = 0
    aux = len(lista) - 1
    #for para percorrer os valores da lista e soma-los, colocando o valor final na lista (resposta),
    #diminuindo o aux (auxiliar) que quando chegar a 0 o for encerra
    for i in lista:
        num_decimal = i * (16 ** aux)
        resultado += num_decimal
        aux -= 1
        if aux < 0:
            resposta.append(resultado)
            break
    #transformei o resultado que ficou armazenado na lista resposta[0] em uma variavel para poder transforma-lo em outra base
    numero_decimal = resposta[0]
    print(f'Seu valor de base octal {entrada_hexa} vale {numero_decimal} na base decimal.')
    return converterdecimal(numero_decimal)
