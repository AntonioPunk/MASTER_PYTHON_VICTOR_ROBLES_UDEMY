""""    Una variable es un contenedor que almacena información
        (texto, números, etc.). Como su propio nombre indica
        esa información puede ser modificada. """

""" CREAR VARIABLES Y REASIGNAR VALORES"""
text = "Soy una variable con nombre `text' y almaceno... texto!!!"
print(text)

number = 2024
print(number)

text = 2024
number = "Ahora 'number' es un texto!!!"

print(f"Ahora 'text' es un número y vale: {text}")
print(number)

decimal = 8.9
print(f"Tambien hay números decimales llamados 'float': {decimal}")

""" CONCATENACIÓN DE VARIABLES Y TEXTO 'FORMATEADO' """

nombre = "Antonio"
apellidos = "Arias Ureta"
telefono = "63045678997"

print(nombre + apellidos) # Así no!!! Las cadenas aparecen juntas.
print(nombre + " " + apellidos) # Es una opción...
print(nombre, apellidos, telefono) # En realidad no es una concatenación.

# Texto formateado, la mejor opción.
print(f"Mi nombre es {nombre} {apellidos} y mi teléfono es {telefono}") 
# Otra forma de formatear texto con el método '.format'
print("Mi nombre es {} {} y mi teléfono es {}".format(nombre, apellidos, telefono))


