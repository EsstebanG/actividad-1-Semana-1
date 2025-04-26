# Ejercicio #4 #
# Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta". #

contraseña = str(input("Digite su contraseña: "))

if contraseña == "python123":
    print("Acceso concedido.")
elif contraseña != "python123":
    print("Contraseña incorrecta.")