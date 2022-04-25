"""Programa para indicar si un número es par o impar"""

print("----------------------------------------------")
print("----------- NÚMEROS PARES O IMPARES ----------")
print("----------------------------------------------")

# input
x=input("Digite el valor de x: ")
x=int (x)

# processing
if x % 2 == 0:
    z = ("El número " + str (x) + " es par ")

else:
    z = ("El número " + str (x) + " es impar ")

# output 
print(z)