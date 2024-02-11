"""
computeSales.py - es un programa que obtiene todas las ventas
consigue cuál es el costo unitario del producto y despliega el
precio total.
"""

import json
import sys
import time


def calcular_precio_total(productos, ventas):
    """
    Es la función que calcula los ingresos totales
    """
    total = 0
    for venta in ventas:
        producto_nombre = venta['Product']
        cantidad = venta['Quantity']
        for producto in productos:
            if producto['title'] == producto_nombre:
                precio_unitario = producto.get('price', 0)
                if isinstance(precio_unitario, (int, float)):
                    if precio_unitario > 0:
                        total += cantidad * precio_unitario
                    else:
                        total += cantidad * precio_unitario * (-1)
                else:
                    print(f"El precio de '{producto_nombre}' está incorrecto.")
                break
    return round(total, 2)


def guardar_total_en_txt(total):
    """
    Función que guarda la respuesta en un txt
    """
    try:
        with open('total.txt', 'w') as file:
            file.write(f"El precio total de las ventas es: ${total:.2f}")
    except ValueError:
        print("Error")


def main():
    """
    función principal
    """
    if len(sys.argv) != 3:
        return
    archivo_productos = sys.argv[1]
    archivo_ventas = sys.argv[2]
    try:
        with open(archivo_productos, 'r') as form:
            productos = json.load(form)
        with open(archivo_ventas, 'r') as form:
            ventas = json.load(form)
    except FileNotFoundError:
        print("No se encontró el archivo especificado.")
        return
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return
    start_time = time.time()
    precio_total = calcular_precio_total(productos, ventas)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("El precio total de las ventas es: $", precio_total)
    print(f"Tiempo de ejecución: {elapsed_time} segundos")
    guardar_total_en_txt(precio_total)


if __name__ == "__main__":
    main()
