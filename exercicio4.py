# criar um programa solicite o raio de uma circunferência,
# calcule e que apresente a área e o comprimento da circunferência

import math
raio = float(input("\nDigitar o raio da circunferência em cm: "))
comprimento = 2 * math.pi * raio
area = math.pi * raio * raio
print("\nO comprimento da circunferência é igual a %.2f cm " % (comprimento),"\n")
print("A área da circunferência é igual a %.2f cm² " % (area),"\n")