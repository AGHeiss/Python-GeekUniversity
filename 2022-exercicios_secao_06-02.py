"""
24 - Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com excessão dele próprio.
Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
===============================================================================================================================================================
valor = int(input('Digite um número inteiro positivo: '))
divisores = []
for divisor in range(1, valor):
    if valor % divisor == 0:
        divisores.append(divisor)
print(divisores, sum(divisores))
================================================================================================================================================================

25 - Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.
================================================================================================================================================================
multiplos = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiplos.append(i)
print(sum(multiplos))
================================================================================================================================================================

26 - Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
================================================================================================================================================================
valor = int(input("Digite um número inteiro positivo: "))
while True:
    entrada11 = valor % 11 == 0
    entrada13 = valor % 13 == 0
    entrada17 = valor % 17 == 0
    if entrada11 or entrada13 or entrada17:
        print(f'O número {valor} é um múltiplo de: 11 {entrada11}; 13 {entrada13}; 17 {entrada17}')
        break
    valor = valor + 1
================================================================================================================================================================

27 - Em matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica:
H(n) = 1 + 1 / 2 + 1 / 3 + 1 / 4 + ... + 1 / n
================================================================================================================================================================
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
contador = 1
valor = 0
harmonica = 0
while valor <= 0:
    valor = int(input("Digite um número inteiro posítivo: "))
while contador <= valor:
    harmonica = harmonica + (1 / contador)
    contador = contador + 1

print(f'O número que você digitou foi {valor}, o número harmônico deste valor é de {harmonica:.4f}.')
================================================================================================================================================================

28 - Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a fórmula a seguir:
E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / N!
================================================================================================================================================================
contador = 1
valor = 0
e = 1

while valor <= 0:
    valor = int(input("Digite qualquer número inteiro positivo: "))

while contador <= valor:
    fatorial = 1
    for n in range(1, contador + 1):
        fatorial *= n 
    e += (1 / fatorial)
    contador += 1

print(f"O resultado do cálculo E é de {e:.2f}")
================================================================================================================================================================

29 - Escreva um programa para calcular o valor da série, para 5 termos.
S = 0 + 1 / 2! + 2 / 4! + 3 / 6! + ...
================================================================================================================================================================
contador = 0
valor = 0
serie = 0
numeroserie = 0
while valor <= 0:
    valor = int(input("Digite um número inteiro positivo: "))
while contador <= valor:
    fatorial = 1
    print(f"Adicionando o fatorial de {contador}")
    for n in range(1, contador+1):
        if contador % 2 == 0:
            fatorial = fatorial * n
        else:
            continue
    print(f"Adicionando a soma {numeroserie} / {fatorial:.2f} para calcular o valor da série.")
    serie = serie + (numeroserie / fatorial)
    numeroserie = numeroserie + 1
    contador += 2
print(f"O valor da série do número escolhido é de: {serie:.2f}")
================================================================================================================================================================

30 - Faça programas para calcular as seguintes sequências:
1 + 2 + 3 + 4 + 5 + 6 + 7 + n;
1 - 2 + 3 - 4 + 5 + ... + (2n - 1)?? # OBS: Números pares negativos e ímpares positivos
1 + 3 + 5 + 7 + ... + (2n - 1)
================================================================================================================================================================
valor = 0
while valor <= 0:
    valor = int(input('Digite um número inteiro positivo: '))

soma1 = 0
soma2 = 0
soma3 = 0

for n in range(1, valor + 1):
    soma1 = soma1 + n

for i in range(1, valor + 1):
    if i % 2 == 0:
        soma2 = soma2 - i
    else:
        soma2 = soma2 + i

for j in range(1, valor + 1):
    sequencia = (j * 2) - 1
    soma3 = soma3 + sequencia

print(f'Os cálculos até o número {valor} são de respectivamente: {soma1}, {soma2}, {soma3}')
================================================================================================================================================================

31 - Faça um programa que calcule e escreva o valor de S
S = 1 / 1 + 3 / 2 +  5 / 3 + 7 / 4 ... 99 / 50
================================================================================================================================================================
denominador = 0
s = 0

for n in range(1, 100, 2):
    denominador += 1
    cal = n / denominador
    print(f'{n} / {denominador}')
    s += cal

print(f'O valor de S é: {s}')
================================================================================================================================================================

32 - Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número de cada dado e a relação entre eles (>, <, =) de cada lançamento
================================================================================================================================================================
from random import randint
valor = 0
while valor <= 0:
    valor = int(input('Digite o número de vezes que os dados serão jogados: '))
while valor > 0:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    if dado1 > dado2:
        print(f'O dado 1 ({dado1}) é maior do que o dado 2 ({dado2}).')
    elif dado1 == dado2:
        print(f'O dado 1 ({dado1}) é igual ao dado 2 ({dado2}).')
    else:
        print(f'O dado 1 ({dado1}) é menor do que dado 2 ({dado2}).')

    valor -= 1
================================================================================================================================================================
33 - Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou ambos. Exemplo:
Para n = 6, i = 2 e j = 3 a saída deverá ser: 0, 2, 3, 4, 6, 8.
================================================================================================================================================================
valor = 0
multiplos = []
while valor <= 0:
    valor = int(input('Digite a quantidade de números que você quer que apareça: '))
i = 2
j = 3
for n in range(0, valor*i*j):
    if n % i == 0:
        multiplos.append(n)
    elif n % j == 0:
        multiplos.append(n)
print(f'{multiplos[0:valor]}')
================================================================================================================================================================
34 - Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20?
Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto
================================================================================================================================================================
valor = 0
multiplo = []
while valor <= 0:
    valor = int(input('Entre com um número inteiro positivo: '))
for n in range(1, valor):
    if n % 1 == 0:
        if n % 2 == 0:
            if n % 3 == 0:
                if n % 4 == 0:
                    if n % 5 == 0:
                        if n % 6 == 0:
                            if n % 7 == 0:
                                if n % 8 == 0:
                                    if n % 9 == 0:
                                        if n % 10 == 0:
                                            if n % 11 == 0:
                                                if n % 12 == 0:
                                                    if n % 13 == 0:
                                                        if n % 14 == 0:
                                                            if n % 15 == 0:
                                                                if n % 16 == 0:
                                                                    if n % 17 == 0:
                                                                        if n % 18 == 0:
                                                                            if n % 19 == 0:
                                                                                if n % 20 == 0:
                                                                                    multiplo.append(n)

print(multiplo)
if multiplo == []:
    print('Você não chegou perto do valor, tente um número mais alto. RESPOSTA: O número que é divisível do número 1 ao 20 é -> (232792560)')
================================================================================================================================================================
35 - Faça um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário define o valor inicial do intervalo e o valor final
deste intervalo e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que
o valor final) deve ser escrito uma mensagem de erro na tela, "Intervalo de valores inválidos" e o programa termina. Exemplo de tela de saída:
Digite o valor inicial e valor final:
================================================================================================================================================================
impares = []
valor1 = 0
valor2 = 0
while valor1 <= 0:
    valor1 = int(input('Digite um número inteiro positivo: '))
while valor2 <= 0:
    valor2 = int(input('Digite um número inteiro positivo maior do que o primeiro: '))
if valor1 <= valor2:
    for n in range(valor1, valor2 + 1):
        if n % 2 != 0:
            impares.append(n)
else:
    print('Intervalo de valores inválidos.')
    exit()

print('A soma dos números impares é:', sum(impares), 'Os números ímpares no intervalo de números escolhido são:', impares)
================================================================================================================================================================
36 - Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da soma.
================================================================================================================================================================
soma = 0
soma2 = 0
for i in range(1, 100+1):
    quadrado = i * i
    soma = soma + quadrado
    soma2 = i + soma2

print(f'A soma dos quadrados é de {soma}, o quadrado da soma é de {soma2*soma2}. A diferença desses valores é de {(soma2*soma2) - soma}.')
================================================================================================================================================================
37 - Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte: a soma dos dois dígitos
de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio numero. Por exemplo, para o inteiro 3025,
temos que:
30 + 25 = 55
55 ** 2 = 3025
================================================================================================================================================================
lista = []
for i in range(1000, 9999 + 1):
    entrada = str(i)
    baixa = int(entrada[0:2])
    alta = int(entrada[2::])
    valor = (baixa + alta) ** 2
    if valor == i:
        lista.append(i)

print(lista)
================================================================================================================================================================

"""




















    






