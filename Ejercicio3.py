precios_articulos = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}
articulo = input("Escribe el nombre del artículo que desees: ")
if articulo in precios_articulos:
    número_unidades = int(input("Introduce el número de unidades deseadas: "))
    precio_total = precios_articulos[articulo] * número_unidades
    print("El precio total de", articulo,"es de",precio_total,"€")
else:
    print("El producto no está en el diccionario")
input("Pulsa enter para salir")
