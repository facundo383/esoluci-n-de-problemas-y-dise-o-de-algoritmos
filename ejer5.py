import hashlib

claves_publicas_rom = {
    "ROM_Code":   "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
    "Bootloader": "a1c5d9a939462d7c00e62846ef320b66b0d9129524582f34ee368d40733d712f",
    "Kernel":     "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
}

def verificar_cadena_arranque(indice_etapa, secuencia_arranque):
    if indice_etapa >= len(secuencia_arranque):
        print("\n[SECURE BOOT] Cadena validada con exito. Sistema iniciado.")
        return True

    bloque_actual = secuencia_arranque[indice_etapa]
    nombre_bloque = bloque_actual["name"]
    datos_bloque = bloque_actual["data"]

    print(f"[SECURE BOOT] Verificando bloque [{indice_etapa + 1}/{len(secuencia_arranque)}]: '{nombre_bloque}'...")
    hash_calculado = hashlib.sha256(datos_bloque.encode('utf-8')).hexdigest()
    hash_esperado = claves_publicas_rom.get(nombre_bloque)

    if hash_calculado != hash_esperado:
        print(f"\n[ALERTA] Firma invalida en '{nombre_bloque}'!")
        print("[SECURE BOOT] ARRANQUE ABORTADO.")
        return False

    print(f"[SECURE BOOT] Bloque '{nombre_bloque}' OK.")
    return verificar_cadena_arranque(indice_etapa + 1, secuencia_arranque)

print("Ejecutando verificacion de arranque...")
secuencia = [
    {"name": "ROM_Code",   "data": "Firmware_Base_v1.0"},
    {"name": "Bootloader", "data": "Stage2_Bootloader_Code"},
    {"name": "Kernel",     "data": "Linux_Kernel_Image_x64"}
]
verificar_cadena_arranque(0, secuencia)