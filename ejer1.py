import time

tamano = 1000

print("Creando la matriz")
matriz = [[1] * tamano for _ in range(tamano)]

print("Calculando por filas")
suma_fila = 0
inicio_fila = time.perf_counter()

for i in range(tamano):
    for j in range(tamano):
        suma_fila += matriz[i][j]

fin_fila = time.perf_counter()
duracion_fila = fin_fila - inicio_fila 

print("Calculando por columnas")
suma_columna = 0
inicio_columna = time.perf_counter()

for j in range(tamano):
    for i in range(tamano):
        suma_columna += matriz[i][j]

fin_columna = time.perf_counter()
duracion_columna = fin_columna - inicio_columna  

print(f"Suma por Filas:    {suma_fila} | Tiempo: {duracion_fila:.6f} s")
print(f"Suma por Columnas: {suma_columna} | Tiempo: {duracion_columna:.6f} s")
