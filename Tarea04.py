# Calificaciones
calif_1 = 10
calif_2 = 7
calif_3 = 4

# Calcular el promedio 
promedio = (calif_1 * 0.15) + (calif_2 * 0.35) + (calif_3 * 0.50)

# Imprimir el promedio
print(f"El promedio ponderado es: {promedio}")

# Matriz original
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

# Corregir la matriz
for fila in matriz:
    # Sumar los primeros tres valores
    suma = sum(fila[:3])
    # Corregir el cuarto valor
    fila[3] = suma

# Imprimir la matriz corregida
print("Matriz corregida:")
for fila in matriz:
    print(fila)