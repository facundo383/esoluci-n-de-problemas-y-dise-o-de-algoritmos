import hashlib
import time

configuracion_sistema_ram = {
    "VOLTAGE_LIMIT_MV": 3300,
    "MAX_TEMP_CELSIUS": 75,
    "OPERATING_MODE": "NORMAL_MODE",
    "WATCHDOG_ENABLED": True
}

def calcular_hash_configuracion(diccionario_config: dict) -> str:

    datos_serializados = str(sorted(diccionario_config.items()))
    return hashlib.sha256(datos_serializados.encode('utf-8')).hexdigest()

def monitorear_integridad_memoria(hash_referencia: str, ciclos: int = 5):

    print("\n INICIANDO BUS DE MONITOREO DE INTEGRIDAD DE MEMORIA ")
    print(f"[GOLDEN HASH ROM] Hash de Referencia: {hash_referencia}\n")

    for i in range(1, ciclos + 1):
        print(f"[CICLO {i}/{ciclos}] Leyendo registros de configuracion en RAM")
        
        if i == 4:
            print("\n[ALERTA DE HARDWARE] Ocurrio un Bit Flip / Inyeccion en RAM!")
            configuracion_sistema_ram["VOLTAGE_LIMIT_MV"] = 4500  
        hash_actual = calcular_hash_configuracion(configuracion_sistema_ram)

        if hash_actual != hash_referencia:
            print("[CRITICO] FALLO DE INTEGRIDAD DE MEMORIA DETECTADO!")
            print(f"  -> Hash Esperado (ROM):  {hash_referencia}")
            print(f"  -> Hash Calculado (RAM): {hash_actual}")
            print("[SISTEMA] Disparando interrupcion NMI y entrando en MODO SEGURO.")
            return False

        print(f"  -> Hash RAM OK: {hash_actual[:16]}... | Estado: SEGURO")
        time.sleep(0.4)

    print("\n[BIST] Pruebas completadas sin detectar corrupcion de memoria.")
    return True

if __name__ == "__main__":

    print("SISTEMA DE MONITOREO DE INTEGRIDAD DE REGISTROS (BIST)")

    hash_dorado = calcular_hash_configuracion(configuracion_sistema_ram)

    monitorear_integridad_memoria(hash_referencia=hash_dorado, ciclos=5)