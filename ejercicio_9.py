# Ejercicio #9 
# Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

año = int(input("Digite su año de nacimiento para saber si es o no año bisiesto: "))


if año %4==0 and año % 400==0:
    print("Su año es bisiesto.")
elif año != 100:
    print("Su año es bisiesto.")
else: 
    print("Su año no es bisiesto.")