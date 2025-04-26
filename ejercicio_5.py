# Ejercicio #5 #
# Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina. #

totalCuenta = int(input("Digite el valor total de la cuenta: "))
porcentaje = int(input("Digite el porcentaje de propina que dejará (10, 15 o 20%): "))


if porcentaje == 10:

    porce10 = totalCuenta * 0.10
    porceTotal10 = totalCuenta + porce10
    print("El total de su factura es", totalCuenta,", su porcentaje es del 10%: ","y el total es: ", porceTotal10)

elif porcentaje == 15:

    porce15 = totalCuenta * 0.15
    porceTotal15 = totalCuenta + porce15
    print("El total de su factura es", totalCuenta,", su porcentaje es del 15% ","y el total es: ", porceTotal15)

elif porcentaje == 20: 

    porce20 = totalCuenta * 0.20
    porceTotal20 = totalCuenta + porce20
    print("El total de su factura es", totalCuenta,", su porcentaje es del 20% ","y el total es: ", porceTotal20)

else:
    print("Haz digitado algún dato icorrectamente.")