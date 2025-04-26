# Ejercicio #7 #
# Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo. #

numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))

if numero1 < numero2:
    print("El número mayor es: ", numero2)
    print("El número menor es: ", numero1)

elif numero1 > numero2:
    print("El número mayor es: ", numero1)
    print("El número menor es: ", numero2)