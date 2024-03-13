import os #serve para limpar o terminal

palavra_secreta = 'PalavraSecreta' # se deixar dentro do while a palavra secreta fica resetando
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite apenas uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada 
        #mas, ate o momento pode ficar sempre ssssss pq s tem na letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta: #letra_secreta é o indice do for (i), é a letra por letra da palavra_secreta
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls') #serve para limpar o terminal
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'A palavra era, {palavra_formada}')
        print(f'Tentativas: {tentativas}')
        palavra_secreta = 'PalavraSecreta' # se deixar dentro do while a palavra secreta fica resetando
        letras_acertadas = ''
        tentativas = 0
