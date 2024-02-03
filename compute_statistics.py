"""
computeStatistics.py - Da las estadísticas de un set de datos.

De acuerdo con los números obtenidos, se saca media, mediana, moda, desviación
estándar y varianza.
"""
import sys
import time
def es_numero(cadena):
    """
    revisa si el valor es decimal.
    """
    try:
        float(cadena)
        return True
    except ValueError:
        print(cadena + " no es número.")
        return False
def leer_archivo_txt(nombre_archivo):
    """
    lee el archivo.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            lista_de_numeros = [
                float(linea.strip()) for linea in lineas if es_numero(linea.strip())
            ]
            return lista_de_numeros
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except OSError as error_found:
        print(f"Error al leer el archivo: {error_found}")
        sys.exit(1)
def mean(lista):
    """
    calcula el promedio.
    """
    total = 0
    for numero in lista:
        total += numero
    return total/len(lista)
def varianza(lista,mean_f):
    """
    calcula la varianza.
    """
    total = 0
    for numero in lista:
        total += (numero - mean_f)**2
    return total/len(lista)
def moda(lista):
    """
    calcula la moda.
    """
    conteo = {}
    for numero in lista:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1
    moda_f = [
        elemento for elemento, frecuencia in conteo.items() if frecuencia == max(conteo.values())
    ]
    if len(moda_f)>1:
        return moda_f[0]
    return moda
def ordenar_lista(lista):
    """
    ordena la lista.
    """
    n_valor = len(lista)
    for i in range(n_valor):
        for j in range(0, n_valor-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
def mediana(lista):
    """
    obtiene la mediana.
    """
    datos_ordenados = ordenar_lista(lista)
    n_valor_m = len(datos_ordenados)
    if n_valor_m % 2 == 0:
        indice_medio_1 = n_valor_m // 2 - 1
        indice_medio_2 = n_valor_m // 2
        mediana_f = (datos_ordenados[indice_medio_1] + datos_ordenados[indice_medio_2]) / 2
    else:
        indice_medio = n_valor_m // 2
        mediana_f = datos_ordenados[indice_medio]
    return mediana_f
def escribir_estadisticas_a_archivo(mean_f,
                                    varianza_f,
                                    desviacion_f,
                                    moda_f,
                                    mediana_f):
    """
    Escribe las estadísticas en un archivo txt.
    """
    with open("resultado.txt", 'w') as archivo_salida:
        archivo_salida.write("ESTADÍSTICA DESCRIPTIVA\n")
        archivo_salida.write("=" * 30 + "\n")
        archivo_salida.write(f"PROMEDIO: {mean_f}\n")
        archivo_salida.write(f"VARIANZA: {varianza_f}\n")
        archivo_salida.write(f"DESVIACIÓN: {desviacion_f}\n")
        archivo_salida.write(f"MODA: {moda_f}\n")
        archivo_salida.write(f"MEDIANA: {mediana_f}\n")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, proporciona el nombre del archivo como argumento.")
        sys.exit(1)
    start_time = time.time()
    numeros_lista = leer_archivo_txt(sys.argv[1])
    if numeros_lista:
        mean_result = mean(numeros_lista)
        varianza_result = varianza(numeros_lista,mean_result)
        desviacion_result = varianza_result**(1/2)
        moda_result = moda(numeros_lista)
        mediana_result = mediana(numeros_lista)
        escribir_estadisticas_a_archivo(mean_result,
                                        varianza_result,
                                        desviacion_result,
                                        moda_result,
                                        mediana_result)
        print("+++++++++++++++++++++++++++++++++++++++")
        print("         ESTADISTICA DESCRIPTIVA       ")
        print("   PROMEDIO:" + str(mean_result))
        print("   VARIANZA:" + str(varianza_result))
        print(" DESVIACION:" + str(desviacion_result))
        print("       MODA:" + str(moda_result))
        print("    MEDIANA:" + str(mediana_result))
        print("+++++++++++++++++++++++++++++++++++++++")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo de ejecucion: {elapsed_time} segundos")
        