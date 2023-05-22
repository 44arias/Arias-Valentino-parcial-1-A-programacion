from funcion1 import*
from funcion2 import*
from funcion3 import*

print("------------------------------------------------")

precio_con_aumento = aplicarAumento(10)

print(precio_con_aumento)

print("------------------------------------------------")

cadena = "Hola, Mundo!"
caracter_a_reemplazar = "o"
caracter_reemplazo = "x"

cadena_reemplazada, cantidad_reemplazos = reemplazarCaracteres(cadena, caracter_a_reemplazar, caracter_reemplazo)

print("Cadena original:", cadena)
print("Cadena reemplazada:", cadena_reemplazada)
print("Cantidad de reemplazos:", cantidad_reemplazos)

print("------------------------------------------------")

cadena_original = "algoritmo"
cadena_ordenada = ordenarCaracteres(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena ordenada:", cadena_ordenada)

