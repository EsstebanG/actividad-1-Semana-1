# Ejercicio #8 #
# Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:

# "Bajo peso" si es menor a 18.5 #
# "Normal" si está entre 18.5 y 24.9 #
# "Sobrepeso" si está entre 25 y 29.9 #
# "Obesidad" si es mayor o igual a 30 #

kg = int(input("Digite su peso actual: "))
m = float(input("Digite su altura actual: "))

imc = kg / (m * m)

if imc < 18.5:
    print("Su indice de masa corporal es: ", imc, "usted se encuentra en estado: Bajo de peso.")

elif imc == 18.5 and imc <= 24.9:
    print("Su indice de masa corporal es: ", imc, "usted se encuentra en estado: Normal.")

elif imc == 25 and imc <= 29.9:
    print("Su indice de masa corporal es: ", imc, "usted se encuentra en estado: Sobrepeso.")
    
elif imc >= 30:
    print("Su indice de masa corporal es: ", imc, "usted se encuentra en estado: Obesidad.")


