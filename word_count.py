"""
wordCount.py - Conteo de palabras en un archivo de texto.

Este script lee un archivo de texto y cuenta la frecuencia de cada palabra,
luego muestra las palabras y sus frecuencias ordenadas de mayor a menor.
"""
import sys
import time
def leer_archivo_txt(nombre_archivo):
    """
    leer archivo de texto
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            lista = [str(linea.strip()) for linea in lineas]
            return lista
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except OSError as error_found:
        print(f"Error al leer el archivo: {error_found}")
        sys.exit(1)
def escribir_resultados_a_archivo(resultados, nombre_archivo_salida="resultados.txt"):
    """
    crea archivo de texto
    """
    with open(nombre_archivo_salida, 'w') as archivo_salida:
        for palabra, frecuencia in resultados:
            archivo_salida.write(f"{palabra}: {frecuencia}\n")
def conteo(palabras):
    """
    conteo manual de las palabras
    """
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
def ordenar_frecuencia(frecuencia):
    """
    ordena las palabras con mayor frecuencia
    """
    frecuencia_ordenada = []
    while frecuencia:
        max_palabra = None
        max_frecuencia = float('-inf')
        for palabra, freq in frecuencia.items():
            if freq > max_frecuencia:
                max_palabra = palabra
                max_frecuencia = freq
        frecuencia_ordenada.append((max_palabra, max_frecuencia))
        del frecuencia[max_palabra]
    return frecuencia_ordenada
def contar_frecuencia_palabras(palabras):
    """
    cuenta la frecuencia de cada palabra
    """
    contador = conteo(palabras)
    return contador
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, proporciona el nombre del archivo como argumento.")
        sys.exit(1)
    start_time = time.time()
    palabras_archivo = leer_archivo_txt(sys.argv[1])
    if palabras_archivo:
        frecuencia_palabras = contar_frecuencia_palabras(palabras_archivo)
        palabras_ordenadas = ordenar_frecuencia(frecuencia_palabras)
        print("{:<15} {:<10}".format("Palabra", "Frecuencia"))
        print("="*25)
        for palabra_ordenada, frecuencia_ordenada_interna in palabras_ordenadas:
            print("{:<15} {:<10}".format(palabra_ordenada, frecuencia_ordenada_interna))
        escribir_resultados_a_archivo(palabras_ordenadas)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo de ejecución: {elapsed_time} segundos")
