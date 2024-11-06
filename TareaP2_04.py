# Melannie Martínez Velasco
# Ejercicio 1: mediante teclado especificar lo siguiente:
# - Número de columnas que tendrá el dataframe
# - Una vez que se especifique, preguntar por los datos que tendrá el data frame
# - Preguntar por los nombres de las columnas que tendrá el dataframe
# - Preguntar por los nombres de las filas que tendrá el dataframe}
# - Una vez introducidos los datos, crear el dataframe que contenga esa información
# - Mostrar el dataframe
import pandas as pd

num_columnas = int(input("Ingrese el número de columnas que tendrá el DataFrame: "))
nombres_columnas = []
nombres_filas = []
datos = []
for x in range(num_columnas):
    nombre_columna = input(f"Ingrese el nombre de la columna {x + 1}: ")
    nombres_columnas.append(nombre_columna)

num_filas = int(input("Ingrese el número de filas que tendrá el DataFrame: "))
for x in range(num_filas):
    nombre_fila = input(f"Ingrese el nombre de la fila {x + 1}: ")
    nombres_filas.append(nombre_fila)
for x in range(num_filas):
    fila_datos = []
    for z in range(num_columnas):
        dato = input(f"Ingrese el dato para {nombres_filas[x]} en la columna {nombres_columnas[z]}: ")
        fila_datos.append(dato)
    datos.append(fila_datos)

df = pd.DataFrame(data=datos, columns=nombres_columnas, index=nombres_filas)
print("\nEl DataFrame creado es:\n")
print(df)