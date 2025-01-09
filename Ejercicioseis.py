"""Ejercicio 6. 
Se   tiene   los   puntos   A   y   B   en   el   cuadrante   positivo   
del   plano   cartesiano, elabore el algoritmo que permita obtener 
la distancia entre A y B. """

"""Solucion: un punto en el plano tiene dos coordenadas (X ,Y), entonces el 
punto A tendrá sus coordenadas (AX, AY) y el punto B de 
manera similar (BX, BY), luego se tiene los siguientes datos:

Para determinar la distancia entre dos puntos, empleamos la 
BX 
Coordenada Y de B   
BY 
65 / 257  ---------------------Mirar formula en la captura de la solucion------------------------------------------ 

Esta fórmula la podemos encontrar en los textos de matemática 
básica o geometría plana. Determinado el proceso de cálculo 
construimos el pseudocódigo. 

INICIO 
Leer (AX) 
Leer (AY ) // se lee las coordenadas del punto A 
Leer ( BX)  
Leer ( BY ) // se lee las coordenadas del punto B 
// Procedemos a realizar el cálculo matemático, el símbolo ^ es 
usado para la potencia 
D  ((AX-BX) ^2 + (AY-BY) ^2) ^0.5 
Escribir ( D ) 
FIN 
Nota: El cálculo de la raíz cuadrada se da usando el símbolo de 
potencia elevado a la 0.5. 
El código del Ejercicio 6 en Python es el siguiente: 



"""

# -*- coding: utf-8 -*- 
#Decoración: Nombre del Algoritmo 
print("-------------------------------------------------------") 
print("Ejercicio6: DISTANCIA ENTRE 2 PUNTOS A y B, en 2D.") 
print("-------------------------------------------------------") 

#Entradas 
print("Ingrese coordenadas del Punto A: ") 
AX = float(input("Ax: ")) 
AY = float(input("Ay: ")) 
print("Ingrese coordenadas del Punto B: ") 
BX = float(input("Bx: ")) 
66 / 257 
BY = float(input("By: ")) 

#Proceso 
D = ( (AX-BX)**2 + (AY-BY)**2 )**0.5 
#Salida 
print("\nSALIDA: ") 
print("-------------------------------------------------------") 
print("Resultado:", D)

""""Ingrese coordenadas del Punto A: 
Ax: 0 
Ay: 0 
Ingrese coordenadas del Punto B: 
Bx: 1 
By: 1 
SALIDA: ------------------------------------------------------- 
Resultado: 1.4142135623730951"""