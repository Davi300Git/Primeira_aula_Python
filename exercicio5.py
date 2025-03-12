# exemplo 5 - a luz, ao incidir num prédio, projeta uma sombra chão, formando 
#um triângulo retângulo como o mostrado na figura abaixo de inclinação dos raios solares,
#calcule e mostre a altura do prédio

#math.radians
#math.tan
import math

sombra = float(input("\nDigite o comprimento da sombra em m: "))
angulo = math.radians(float(input("\nDigite o angulo em graus: ")))
altura = math.tan(angulo * sombra)
print("\nA altura do prédio é de %.2f m" % (altura),"\n")