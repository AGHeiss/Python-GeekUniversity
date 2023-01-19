"""
38 - Faça um programa que calcule o terno pitagórico a, b, c, para o qual a + b + c = 1000. Um terno pitagórico é um conjunto de três números naturais, a, b, c, para a qual,
a² + b² = c²
Por exemplo,
3² + 4² = 9 + 16 = 25 = 5²
================================================================================================================================================================
import math
for a in range(1, 500):
    for b in range(1, 500):
        c = math.sqrt(a ** 2 + b ** 2)
        if a + b + c == 1000:
            print(a, b, c)
================================================================================================================================================================
39 - Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário. Esse programa não pode permitir a entrada de dados inválidos, ou seja,
medidas menores ou iguais a 0.
================================================================================================================================================================
base = 0
altura = 0
while base <= 0:
    base = int(input('Digite o valor da base do triângulo: '))
while altura <= 0:
    altura = int(input('Digite o valor da altura desse triângulo: '))
area = (base * altura) / 2
print(f'A area desse triângulo de base {base} e altura {altura}, é de {area}.')
================================================================================================================================================================
40 - Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.
================================================================================================================================================================
numero = 0
lista = []
while numero >= 0:
    numero = int(input('Digite um número inteiro positivo, ou um número negativo para parar: '))
    if numero >= 0:
        lista.append(numero)

if lista != []:
    print(f'O número maior digitado é {max(lista)}, e o número menor é {min(lista)}. Foram digitados {len(lista)} números.')
================================================================================================================================================================
41 - Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado. O programa fica pedindo estes valores
e calculando até que o usuário entre com um valor para resistência igual a zero
R = (R1 * R2) / (R1 + R2)
================================================================================================================================================================
resistor1 = 0
resistor2 = 0
while True:
    resistor1 = int(input('Digite o valor do primeiro resitor: '))
    resistor2 = int(input('Digite o valor do segundo resistor: '))
    if resistor1 <= 0:
        print('A resistência tem valor negativo ou é igual a 0.')
        break
    elif resistor2 <= 0:
        print('A resistência tem valor negativo ou é igual a 0.')
        break

    paralelo = (resistor1 * resistor2) / (resistor1 + resistor2)
    
    print(f'O valor dessa resistência em paralelo é igual a {paralelo}.')

    if paralelo == 0:
        print('A resistência é igual a 0.')
        break
================================================================================================================================================================
42 - Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize
a entrada de dados com um valor negativo ou zero.
================================================================================================================================================================
import math
while True:
    valor = int(input('Digite um número inteiro positivo, ou um numero negativo ou zero para parar: '))
    if valor > 0:
        quadrado = valor ** 2
        cubo = valor ** 3
        raiz = math.sqrt(valor)
        print(f'O valor escolhido de {valor}, possui um quadrado, cubo e raiz quadrada respectivamente de: {quadrado}, {cubo}, {raiz}.')
    else:
        print('Valor igual a zero ou negativo.')
        break
================================================================================================================================================================
43 - Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade 0), e calcule a idade média desse grupo.
================================================================================================================================================================
idade = []
contador = 0
while True:
    valor = int(input(f'Digite a {contador+1}ª idade, ou zero para sair: '))
    if valor > 0:
        idade.append(valor)
        print(f'{len(idade)} indivíduo(s) cadastrado(s), a média da(s) idade(s) é de {sum(idade) / len(idade)}')
    else:
        print('Você informou o número zero ou um número negativo.')
        break
    contador += 1
================================================================================================================================================================
44 - Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior ao número lido. Exemplo: Se o usuário informou o número
30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34
================================================================================================================================================================
fibonacci = [0, 1]
a = 0
b = 1
c = 0
valor = 0
while valor <= 0:
    valor = int(input('Digite um número inteiro positivo: '))
while True:
    c = a + b
    fibonacci.append(c)
    a = b
    b = c
    if c > valor:
        break
print(f"A sequência fibonacci até passar o número digitado é: {fibonacci}")
================================================================================================================================================================
45 - Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa. Você deve criar um menu com as duas opções de conversão e com uma opção
para finalizar o programa. O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado quando a opção de finalizar for escolhida.
================================================================================================================================================================
import time
while True:
    time.sleep(3)
    print('====================')
    print('=======/MENU\=======')
    print('Digite 0 para converter km/h para m/s.')
    print('Digite 1 para converter m/s para km/h.')
    print('Digite 2 para finalizar o programa.')
    print('====================')
    print('====================')

    valor = int(input('Digite a opção escolhida: '))
    if valor == 0:
        velocidade = float(input('Digite a velocidade em km/h: '))
        metros = velocidade / 3.6
        print(f'A velocidade de {velocidade}km/h equivale a {metros:.2f}m/s.\n')
    elif valor == 1:
        velocidade = float(input('Digite a velocidade em m/s: '))
        km = velocidade * 3.6
        print(f'A velocidade de {velocidade}m/s equivale a {km:.2f}km/h.\n')
    else:
        print('Fim do programa.')
        break
================================================================================================================================================================
46 - Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o número que foi gerado, a cada tentativa o programa deverá informar
se o chute é menor ou maior que o número gerado. O programa acaba quando o usuário acerta o número gerado.
O programa deve informar em quantas tentativas o número foi descoberto.
================================================================================================================================================================
import random
numero = random.randint(1, 1000)
print('Foi gerado um número aleatório entre 1 e 1000, descubra qual é!')
tentativas = []
while True:
    valor = int(input(f'Escolha um número aleatório entre 1 e 1000: '))
    tentativas.append(valor)
    if valor > numero:
        print('O número que você digitou é MAIOR do que o número aleatório gerado.')
    if valor < numero:
        print('O número que você digitou é MENOR do que o número aleatório gerado.')
    if valor == numero:
        print(f'Você acertou! É o número {valor}! Você chegou no resultado depois de {len(tentativas)} tentativas.')
        break
================================================================================================================================================================
47 - Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
- Adição (opção 1)
- Subtração (opção 2)
- Multiplicação (opção 3)
- Divisão (opção 4)
- Saída (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida
a opção de saída (opção 5).
================================================================================================================================================================
import time
while True:
    time.sleep(3)
    print('=============================')
    print('====  Escolha o cálculo  ====')
    print('===== Adição - Opção 1 ======')
    print('==== Subtração - Opção 2 ====')
    print('== Multiplicação - Opção 3 ==')
    print('===== Divisão - Opção 4 =====')
    print('====== SAIR - Opção 5 =======')
    print('=============================')
    opcao = int(input('Digite a opção escolhida: '))
    if opcao == 1:
        print('Você escolheu ADIÇÃO!')
        valor1 = int(input('Escolha o primeiro número para realizar o cálculo de adição: '))
        valor2 = int(input('Escolha o segundo número para realizar o cálculo de adição: '))
        resultado = valor1 + valor2
        print(f'O resultado da soma de {valor1} + {valor2} é igual a {resultado}\n')
    elif opcao == 2:
        print('Você escolheu SUBTRAÇÃO!')
        valor1 = int(input('Escolha o primeiro número para realizar o cálculo de subtração: '))
        valor2 = int(input('Escolha o segundo número para realizar o cálculo de subtração: '))
        resultado = valor1 - valor2
        print(f'O resultado da subtração de {valor1} - {valor2} é igual a {resultado}\n')
    elif opcao == 3:
        print('Você escolheu MULTIPLICAÇÃO')
        valor1 = int(input('Escolha o primeiro número para realizar o cálculo de multiplicação: '))
        valor2 = int(input('Escolha o segundo número para realizar o cálculo de multiplicação: '))
        resultado = valor1 * valor2
        print(f'O resultado da multiplicação de {valor1} * {valor2} é igual a {resultado}\n')
    elif opcao == 4:
        print('Você escolheu DIVISÃO')
        valor1 = int(input('Escolha o primeiro número para realizar o cálculo de divisão (numerador): '))
        valor2 = int(input('Escolha o segundo número para realizar o cálculo de divisão (denominador): '))
        resultado = valor1 / valor2
        print(f'O resultado da divisão de {valor1} / {valor2} é igual a {resultado}\n')
    else:
        print('O PROGRAMA SERÁ FINALIZADO.')
        break
================================================================================================================================================================
48 - Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos valores não ultrapassem quatro milhões.
================================================================================================================================================================
par = [0]
a = 0
b = 1
while True:
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        par.append(c)
    if c >= 4000000:
        break
print("Valores pares da sequência fibonacci:", par, "Soma dos valores pares menores do que 4 milhões:", sum(par))
================================================================================================================================================================
49 - O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário. Carlos gosta de fazer aplicações
na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês. João aplicará seu salário integralmente nela, pois está
rendendo 5% ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor
pertencente a Carlos. Teste com outros valores para as taxas.
================================================================================================================================================================
x = 1 #Valor do salário 
carlos = x * 3 #Salário de Carlos
joao = x # Salário de João
apliccarlos = 0
aplicjoao = 0
meses = 0
meta = False
while meta == False:
    apliccarlos = (apliccarlos + carlos) * 1.02
    aplicjoao = (aplicjoao + joao) * 1.05
    meses += 1
    meta = aplicjoao >= apliccarlos
    print(f'{meses}º mês: \n Carlos -> R${apliccarlos:.2f} \n João -> R${aplicjoao:.2f}')

print(f'Aplicando todos os meses. Levará {meses} meses para que João fique com o valor de R${aplicjoao:.2f} e Carlos com o valor de R${apliccarlos:.2f}')
================================================================================================================================================================
50 - Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 e cresce 3 centímetros por ano. Escreva um programa que calcule e imprima
quantos anos serão necessários para que Zé seja maior que Chico.
================================================================================================================================================================
chico = 1.5 #Altura Chico
ze = 1.1 #Altura Zé
anos = 0 #Varíavel para contar os anos
while chico > ze: #Loop enquanto Chico for maior que Zé
    chico = chico + 0.02 #Crescimento do Chico por ano
    ze = ze + 0.03 #Crescimento do Zé por ano
    anos += 1 #Contagem dos anos enquanto o loop for verdadeiro
    print(f'{anos}º ano: \n  Altura Chico -> {chico:.2f}m \n   Altura Zé -> {ze:.2f}m')

print(f'Demorou {anos} anos para que Zé ficasse maior que Chico.')
================================================================================================================================================================
51 - Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre
correspondem ao dobro do ano anterior. Faça programa que determine o salário atual do funcionário.
================================================================================================================================================================
salario = 2030 #Salário inicial de 1996
ano = 1996
aumento = 0.015

while ano <= 2023:
    aumento = aumento * 2
    salario = (salario * aumento) + salario
    ano += 1
    print(f'No ano de {ano}, o salário era de R${salario:.2f} com um aumento de {(aumento * 100):.2f}%.')

================================================================================================================================================================
52 - Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias
para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
================================================================================================================================================================
saque = 0
while saque <= 0:
    saque = int(input('Digite o valor do saque em reais: '))
#Variáveis para contar as notas para o saque
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

notas = saque #Variável para o cálculo das notas sobre o saque

while notas > 0:
    if notas >= 100:
        notas -= 100
        notas100 += 1
    else:
        if notas >= 50:
            notas -= 50
            notas50 += 1
        else:
            if notas >= 20:
                notas -= 20
                notas20 += 1
            else:
                if notas >= 10:
                    notas -= 10
                    notas10 += 1
                else:
                    if notas >= 5:
                        notas -= 5
                        notas5 += 1
                    else:
                        if notas >= 2:
                            notas -= 2
                            notas2 += 1
                        else:
                            if notas >= 1:
                                notas -= 1
                                notas1 += 1

print(f"Para o saque desse valor R${saque}, você receberá {notas1 + notas10 + notas100 + notas2 + notas20 + notas5 + notas50} notas, elas estão divididas em:")

print(f'{notas100} notas de 100.')
print(f'{notas50} notas de 50.')
print(f'{notas20} notas de 20.')
print(f'{notas10} notas de 10.')
print(f'{notas5} notas de 5.')
print(f'{notas2} notas de 2.')
print(f'{notas1} notas de 1.')
================================================================================================================================================================
"""



    
   








    






