#Calculadora de Baskhara
import math

a = int(input())
b = int(input())
c = int(input())

delta = (b**2) - 4*a*c


if delta < 0:
    print("A função NÃO possui raizes reais")
    print ("O valor de Delta = %d"%delta)
    
elif delta >= 0:        
    raizDelta = math.sqrt(delta)
    x1 = (-b+raizDelta)/2*a
    x2 = (-b-raizDelta)/2*a
    print ("O valor de X1 =",x1)
    print ("O valor de X2 =",x2)
    print ("O valor de Delta = %d"%delta)
    




