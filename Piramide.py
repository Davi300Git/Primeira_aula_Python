#Faça um programa em Python que calcule e mostre o valor do volume do tronco de uma pirâmide,
#  para isso o programa deve solicitar ao usuário os valores da altura do tronco da pirâmide (h),
#  o valor da base menor (Bmenor) e o da base maior (Bmaior) e calcular a seguinte expressão:
 #volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5) 

altura = float(input("\nDigite a altura: "))
Bmenor = float(input("\nDigite a base menor: "))
Bmaior = float(input("\nDigite a base maior: "))
volume = altura/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.05)

print("\nO volume é %.2f cm" % (volume))
