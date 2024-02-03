"""
convertNumbers.py - Convierte los números a binarios y hexadecimales.

Este script lee un archivo de texto y convierte los números a binarios y hexadecimales,
luego muestra los números y sus conversiones.
"""
import sys
import time
def es_numero(cadena):
    """
    revisa si es número entero.
    """
    try:
        numero_original = int(cadena)
        numero_convertido = int(float(cadena))
        if numero_original == numero_convertido:
            return True
        print(cadena + " no es un número entero.")
        return False
    except ValueError:
        print(cadena + " no es número.")
        return False
def cambiar_ceros(respuesta):
    """
    los unos los hace ceros y viceversa.
    """
    respuesta_binaria = ""
    for _, bit in enumerate(respuesta):
        if bit == "0":
            respuesta_binaria = respuesta_binaria + "1"
        else:
            respuesta_binaria = respuesta_binaria + "0"
    return respuesta_binaria
def convertir_binario_normal(numero):
    """
    Convierte un número entero positivo a binario.
    """
    respuesta = ""
    while numero > 0:
        bit = 0 if numero % 2 == 0 else 1
        respuesta = str(bit) + respuesta
        numero //= 2
    if len(respuesta) < 4:
        respuesta = "0" * (4 - len(respuesta)) + respuesta
    else:
        respuesta = "0" * (len(respuesta) % 4) + respuesta
    return respuesta
def sumar_uno(respuesta):
    """
    suma 1 a un número binario string.
    """
    carry = 1
    respuesta_nueva = ""
    for i in range(len(respuesta)-1, -1, -1):
        if carry == 1:
            if respuesta[i] == "1":
                respuesta_nueva = "0" + respuesta_nueva
            else:
                carry = 0
                respuesta_nueva = "1" + respuesta_nueva
        else:
            respuesta_nueva = respuesta[i] + respuesta_nueva
    if carry == 1:
        respuesta_nueva = "1" + respuesta_nueva
    return respuesta_nueva
def llenar_doce_unos(respuesta):
    """
    llena 12 espacios si faltan en un string con unos.
    """
    if len(respuesta) < 12:
        return "1" * (12 - len(respuesta)) + respuesta
    return respuesta
def llenar_doce_efes(respuesta):
    """
    llena 12 espacios si faltan en un string con F.
    """
    if len(respuesta) < 12:
        return "F" * (12 - len(respuesta)) + respuesta
    return respuesta
def binario_a_hex(respuesta):
    """
    pasa de binario a hexadecimal.
    """
    respuesta = respuesta.zfill((len(respuesta) + 3) // 4 * 4)
    grupos = [respuesta[i:i+4] for i in range(0, len(respuesta), 4)]
    hexadecimal = ''.join(mapeo_hexadecimal(grupo) for grupo in grupos)
    return hexadecimal.upper()
def mapeo_hexadecimal(grupo):
    """
    Conversiones de grupos de 4 en binario a hexadecimal.
    """
    mapeo = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }
    return mapeo[grupo]
def bin_hex(numero):
    """
    obtiene binario y hexadecimal.
    """
    if numero < 0:
        numero = numero * -1
        binario_normal = convertir_binario_normal(numero)
        binario_invertido = cambiar_ceros(binario_normal)
        respuesta_binaria = sumar_uno(binario_invertido)
        respuesta_hexadecimal = binario_a_hex(respuesta_binaria)
        respuesta_hex_completa = llenar_doce_efes(respuesta_hexadecimal)
        respuesta_completa = llenar_doce_unos(respuesta_binaria)
        return respuesta_completa + " - " + respuesta_hex_completa
    binario_normal = convertir_binario_normal(numero)
    hexadecimal_normal = convertir_hexadecimal(numero)
    return binario_normal + " - " + hexadecimal_normal
def convertir_hexadecimal(num):
    """
    Convierte un número entero a hexadecimal.
    """
    hex_chars = "0123456789ABCDEF"
    resultado = ""
    while num > 0:
        resultado = hex_chars[num % 16] + resultado
        num //= 16
    return resultado
def escribir_lista_a_archivo(numeros, nombre_archivo_salida="resultado.txt"):
    """
    Escribe los resultados en un txt.
    """
    with open(nombre_archivo_salida, 'w') as archivo_salida:
        archivo_salida.write("NUM - BIN - HEX\n")
        archivo_salida.write("="*20 + "\n")
        for numero in numeros:
            resultado = bin_hex(numero)
            archivo_salida.write(f"{resultado}\n")
def leer_archivo_txt(nombre_del_archivo):
    """
    lee el archivo txt
    """
    try:
        with open(nombre_del_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            lista_de_numeros = [int(linea.strip()) for linea in lineas if es_numero(linea.strip())]
            return lista_de_numeros
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except OSError as error_found:
        print(f"Error al leer el archivo: {error_found}")
        sys.exit(1)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, proporciona el nombre del archivo como argumento.")
        sys.exit(1)
    start_time = time.time()
    nombre_archivo = sys.argv[1]
    numeros_leidos = leer_archivo_txt(nombre_archivo)
    if numeros_leidos:
        escribir_lista_a_archivo(numeros_leidos)
        print("{:<10} {:<14} {:<14}".format("NUM", "BIN", "HEX"))
        print("="*45)
        for numero_de_lista in numeros_leidos:
            print("{:<10} {:<14} {:<14}"
                  .format(numero_de_lista, *bin_hex(numero_de_lista)
                  .split(" - ")))
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo de ejecución: {elapsed_time} segundos")
