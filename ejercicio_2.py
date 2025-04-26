# Ejercicio #2 #
# Pide un número al usuario. Di si es positivo, negativo o si es cero. #

numero = int(input("Digite un número cualquiera: "))

if numero == 0:
    print("Su número es cero.")
elif numero < 0:
    print("Su número es negativo.")
elif numero > 0:
    print("Su número es positivo.")
else: 
    print("ERROR.")