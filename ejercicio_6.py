# Ejercicio #6 #
# Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto. #

numSecreto = int(input("Digita un número entre el 1 y el 100, adivina cual es el número secreto: "))


if numSecreto == 0: 
    print("El número no puede ser 0.")

elif numSecreto < 0:
    print("ERROR. Haz escrito un número que no está dentro del rango.")

elif numSecreto > 100:
    print("ERROR. Haz escrito un número que no está dentro del rango.")

elif numSecreto > 77: 
    print("Sigue intentando, este número es mayor que el secreto.")

elif numSecreto < 77:
    print("Sigue intentando, este número es menor que el secreto.")

else:
    print("Felicidades. Haz descubierto el número secreto.")
