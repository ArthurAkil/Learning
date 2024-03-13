def main(): 
    entrada_notas, entrada_centavos = map(int, input().split('.'))
    entrada_centavos = entrada_centavos + entrada_notas * 100

    print('NOTAS:')
    print(f'{(entrada_centavos // 10000)} nota(s) de R$ 100.00')
    entrada_centavos = entrada_centavos % 10000
    print(f'{(entrada_centavos // 5000)} nota(s) de R$ 50.00')
    entrada_centavos = entrada_centavos % 5000
    print(f'{(entrada_centavos // 2000)} nota(s) de R$ 20.00')
    entrada_centavos = entrada_centavos % 2000
    print(f'{(entrada_centavos // 1000)} nota(s) de R$ 10.00')
    entrada_centavos = entrada_centavos % 1000
    print(f'{(entrada_centavos // 500)} nota(s) de R$ 5.00')
    entrada_centavos = entrada_centavos % 500
    print(f'{(entrada_centavos // 200)} nota(s) de R$ 2.00')
    entrada_centavos = entrada_centavos % 200
    print('MOEDAS:')
    print(f'{(entrada_centavos // 100)} moeda(s) de R$ 1.00')
    entrada_centavos = entrada_centavos % 100
    print(f'{(entrada_centavos // 50)} moeda(s) de R$ 0.50')
    entrada_centavos = entrada_centavos % 50
    print(f'{(entrada_centavos // 25)} moeda(s) de R$ 0.25')
    entrada_centavos = entrada_centavos % 25
    print(f'{(entrada_centavos // 10)} moeda(s) de R$ 0.10')
    entrada_centavos = entrada_centavos % 10
    print(f'{(entrada_centavos // 5)} moeda(s) de R$ 0.05')
    entrada_centavos = entrada_centavos % 5
    print(f'{(entrada_centavos // 1)} moeda(s) de R$ 0.01')
    entrada_centavos = entrada_centavos % 1
main()
