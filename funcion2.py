
# Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres 
# como primer parámetro, un carácter como segundo y otro carácter  como tercero,  la misma deberá 
# reemplazar cada ocurrencia del segundo parámetro por el tercero y devolver la cantidad de veces 
# que se reemplazo ese carácter  en la cadena.
def reemplazarCaracteres(cadena: str, caracter_a_reemplazar: str, caracter_reemplazo: str):
    cadena_reemplazada = cadena.replace(caracter_a_reemplazar, caracter_reemplazo)
    cantidad_reemplazos = 0
    for i in cadena:  # Recorre la cadena
        if i == caracter_a_reemplazar:  # Si el caracter es igual al i se reemplaza
            cadena_reemplazada += caracter_reemplazo  # Agrega el caracter de reemplazo a la cadena reemplazada
            cantidad_reemplazos += 1  # Incrementa el contador de reemplazos
        else:  # Si el caracter no es igual al caracter a reemplazar
            cadena_reemplazada += i  # Agrega el caracter original a la cadena reemplazada
    return cadena_reemplazada, cantidad_reemplazos




