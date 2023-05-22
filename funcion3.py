# 3. Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro  y su responsabilidad 
# es ordenar los caracteres de manera ascendente dentro de la cadena. Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"


def ordenarCaracteres(cadena: str):
    caracteres = list(cadena)  # Convierte la cadena en una lista de caracteres
    caracteres.sort()  # Ordena de manera ascendente
    cadena_ordenada = ''.join(caracteres)  # Convierte la lista de caracteres ordenados nuevamente en una cadena
    return cadena_ordenada

