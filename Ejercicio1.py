diccionario = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
divisa = input("Introduce la divisa que deseas: ")
if divisa in diccionario:
    simbolo = diccionario[divisa]
    print("El símbolo de", divisa, "es " + simbolo)
else:
    print("No se encuentra la divisa introducida")
input("Pulsa enter para salir")
