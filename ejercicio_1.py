# Ejercicio #1 #
# Pide al usuario su edad. Si tiene 18 años o más, imprime "Eres mayor de edad". Si no, imprime "Eres menor de edad". #

nombre = input("Digite su nombre: ")
apellido = input("Digite sus apellidos: ")
edad = int(input("Digite su edad: "))
correo = input("Digite su correo eletrocnico en uso: ")

if edad >= 18:
    print("Sus datos son los siguientes:", nombre,",", apellido, ",", correo,",", edad, "eres mayor de edad")
else:
    print("Sus datos son los siguientes:", nombre,",", apellido, ",", correo,",", edad, "eres menor de edad")



