# Ejercicio #10 
# Pide un número al usuario. Di si está dentro del rango de 1 a 10 (inclusive).

num = int(input("Digite un número del 1 al 10: "))

if num <= 0 or num > 10:
    print("Su número está por fuera del rango.")
else: 
    print("Su número está dentro del rango.")