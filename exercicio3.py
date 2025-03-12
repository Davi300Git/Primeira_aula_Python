# Exemplo 3 - vamos criar um programa solicite um numero real, calcule e que apresente: 
# a) o valor absoluto; b) somente sua parte inteira; c) sua raiz quadrada; d) o fatorial desse número

import math
num = float(input("Digite um número "))
absoluto = math.fabs(num)
inteiro = math.trunc(num)
raiz = math.sqrt(num)
fatorial = math.factorial(math.trunc(inteiro))
print("O valor absoluto de",num,"é:",absoluto)
print("O valor inteiro é:", inteiro)
print("O valor raiz é:", raiz)
print("O valor fatorial é:", fatorial)


