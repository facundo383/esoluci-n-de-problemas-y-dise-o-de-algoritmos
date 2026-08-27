import time

tamano_datos = 10_000        
tamano_bloque = 500           
latencia_bus = 0.0005       
datos = list(range(tamano_datos))

print("Iniciando transferencia elemento por elemento...")
destino_elemento = []
inicio_elemento = time.perf_counter()

for item in datos:
    time.sleep(latencia_bus)
    
    destino_elemento.append(item * 2)

fin_elemento = time.perf_counter()
duracion_elemento = fin_elemento - inicio_elemento


print("Iniciando transferencia por bloques (Buffering)...")
destino_bloque = []
inicio_bloque = time.perf_counter()

for i in range(0, tamano_datos, tamano_bloque):
    
    buffer = datos[i : i + tamano_bloque]
    
    buffer_procesado = [item * 2 for item in buffer]
    destino_bloque.extend(buffer_procesado)

fin_bloque = time.perf_counter()
duracion_bloque = fin_bloque - inicio_bloque


print(f"Elementos procesados: {tamano_datos}")
print(f"Tamano de bloque:     {tamano_bloque} elementos")
print(f"Elemento por Elemento: {duracion_elemento:.4f} s | Transacciones en bus: {tamano_datos}")
print(f"Por Bloques (Buffer):  {duracion_bloque:.4f} s | Transacciones en bus: {tamano_datos // tamano_bloque}")
print(f"El procesamiento por bloques fue {duracion_elemento / duracion_bloque:.2f} veces mas rapido.")