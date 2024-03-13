frase = input('Digite uma frase: ')
frase_sem_espaco = frase.replace(' ','')
i = 0
letras = ''
letra_atual = ''
letra_maior = ''
repeticoes = 0
valor_maior = 0

while i < len(frase_sem_espaco):
    if frase_sem_espaco[i] in letras:
        i += 1
        continue
    else:
        letras += frase_sem_espaco[i]
        letra_atual = frase_sem_espaco[i].lower()
        repeticoes = frase_sem_espaco.count(letra_atual)
        if repeticoes > valor_maior:
            valor_maior = repeticoes
            letra_maior = letra_atual
            i += 1
            continue
        else:
            i += 1
            continue

print(f'A letra que mais se repetiu foi "{letra_maior}", ela se repetiu {valor_maior} vezes.')
