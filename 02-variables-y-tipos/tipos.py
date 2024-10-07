""" TIPOS DE DATOS ---------------------------------------------------------------"""

# None (no contiene nada). Su valor se tomará en un condicional como 'False'.
print("------------------------------------------------------------------------")
nada = None
print(nada)
# Mostramos el tipo de dato con 'type()':
print(type(nada))

# Cadena
print("------------------------------------------------------------------------")
cadena = "Hola, soy Antonio"
print(cadena)
print(type(cadena))

# Entero
print("------------------------------------------------------------------------")
entero = 23
print(entero)
print(type(entero))

# Decimal
print("------------------------------------------------------------------------")
decimal = 34.78
print(decimal)
print(type(decimal))

# Booleano. Admite 2 estados: 'True' ó 'False' SIEMPRE CON INICIO EN MAYÚSCULAS!!!
print("------------------------------------------------------------------------")
booleano = True
print(booleano)
booleano = False
print(booleano)
print(type(booleano))

# Lista. Representa a una colección de datos, de cualquera de los
# mostrados anteriormente.
# Se representa con corchetes: []
# Accedemos a cada dato con el subíndice: 'name_list[n]'
print("------------------------------------------------------------------------")
lista = ["Antonio", 47, 1.76, False, None]
print(lista)
print(type(lista))
# Ejemplo de uso:
print(f"El cliente {lista[0]} tiene {lista[1]} años y mide {lista[2]}m.")
print(f"¿Está casado? {lista[3]} - El nombre de su mujer es: {lista[4]}")

# Tupla. Es inmutable, no podemos variar su contenido.
# Se representa con paréntesis: () pero lo que la define es la coma:
print("------------------------------------------------------------------------")
tupla = 34, # Síiiii, esto es una tupla.
print(tupla)
print(type(tupla))
tupla = ("Antonio", 47)
print(tupla)
print(tupla[1]) # Accedemos a sus elementos igual que con las listas.

# Diccionarios. Son listas de datos referenciados por 'clave':'valor'.
# Se representan entre llaves: {}
# Se accede a cada valor mediante su clave.
print("------------------------------------------------------------------------")
diccionario = {"nombre": "Antonio",
               "edad": 47,
               "peso": 78}
print(diccionario)
print(type(diccionario))
print(f"El nombre del cliente es {diccionario["nombre"]} y su peso {diccionario["peso"]}Kg.")

# Sets ó conjuntos.
# Se representan entre llaves: {}
# Sus elementos NO están ordenados y por tanto no podemos acceder a ellos mediante índices.
# Sus elementos NO se repiten. Si existen elementos repetidos Python los toma como 1 solo.
print("------------------------------------------------------------------------")
conjunto = {2, 4, 1, 6, 10, 2, 1, 40}
print(conjunto)
print(type(conjunto))
print(2 in conjunto) # Como 2 está en el conjunto nos mostrará por pantalla 'True'

# Rango. Almacena un rango en una especie de tupla.
print("------------------------------------------------------------------------")
rango = range(2,5)
print(rango)
print(type(rango))
# Ejemplo de aplicación en un ciclo 'for':
for i in rango:
    print(i)
    

""" CONVERTIR UN TIPO DE DATO A OTRO -------------------------------------------------"""
print("------------------------------------------------------------------------")
nombre = "Antonio"
print(nombre)
print(type(nombre))
numero = 47
print(numero)
print(type(numero))

# Si entento concatenar 'nombre' con 'numero' me lanza un ERROR.
# print(nombre + " " + numero)
# Esto sucede porque solo se puden concatenar cadenas de caracteres 'str'
# La solución es convertir 'numero' de entero (int) a cadena (str)
# Esto se hace mediante lo que denominamos 'casteo':
numero = str(numero) # Convertimos número a (str)
print(type(numero))
print(nombre + " " + numero)
# NOTA IMPORTANTE:
# Si hacemos el casteo dentro de la función 'print' nos permiteç
# concatenar las 2 variables PERO el número sigue siendo (int).
numero2 = 47
print(nombre + " " + str(numero2))
print(type(numero2))

# Otra utilidad puede ser para modificar el contenido de una tupla.
# Convertimos la tupla en lista, modificamos el valor que queramos
# y la volvemos a convertir en tupla:
print("------------------------------------------------------------------------")
tupla = (1, 3, 3)
print(tupla)
print(type(tupla))
# tupla[1] = 2  Esta línea de código nos lanzaría un error ya que no
                # podemos modificar los valores de una tupla.
tupla = list(tupla)
print(tupla)
print(type(tupla))
tupla[1] = 2
tupla = tuple(tupla)
print(tupla)
print(type(tupla))
