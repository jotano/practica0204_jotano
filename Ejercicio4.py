info_persona = {}
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
sexo = input("Introduce tu sexo: ")
telefono = input("Introduce tu número de teléfono: ")
correo = input("Introduce tu correo electrónico: ")

info_persona["Nombre"] = nombre
info_persona["Edad"] = edad
info_persona["Sexo"] = sexo
info_persona["Teléfono"] = telefono
info_persona["Correo electrónico"] = correo
print("Éstos son los datos introducidos:", info_persona)
input("Pulsa enter para salir")
