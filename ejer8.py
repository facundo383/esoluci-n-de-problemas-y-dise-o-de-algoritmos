import random
import time

class sistema_gestion_termica:
    def __init__(self, t0_frio: float = 60.0, t1_caliente: float = 85.0):
        self.t0_frio = t0_frio
        self.t1_caliente = t1_caliente
        self.frecuencia_maxima_ghz = 3.5
        self.frecuencia_reducida_ghz = 1.6
        self.frecuencia_actual_ghz = self.frecuencia_maxima_ghz
        self.esta_reducido = False
        self.temp_actual = 55.0

    def leer_sensor_temperatura(self) -> float:
        factor_calor = 2.5 if not self.esta_reducido else -1.8
        delta = random.uniform(-0.5, factor_calor)
        self.temp_actual = max(45.0, min(95.0, self.temp_actual + delta))
        return round(self.temp_actual, 2)

    def evaluar_politica_termica(self, temp: float):
        if temp >= self.t1_caliente and not self.esta_reducido:
            self.esta_reducido = True
            self.frecuencia_actual_ghz = self.frecuencia_reducida_ghz
            print(f"[ALERTA TERMICA] Temp: {temp} C >= T1 ({self.t1_caliente} C) -> ACTIVANDO THROTTLING ({self.frecuencia_reducida_ghz} GHz)")

        elif temp <= self.t0_frio and self.esta_reducido:
            self.esta_reducido = False
            self.frecuencia_actual_ghz = self.frecuencia_maxima_ghz
            print(f"[RECUPERACION] Temp: {temp} C <= T0 ({self.t0_frio} C) -> RESTABLECIENDO RENDIMIENTO ({self.frecuencia_maxima_ghz} GHz)")

        else:
            estado = "THROTTLED" if self.esta_reducido else "NORMAL"
            print(f"[MONITOR] Temp: {temp} C | Frecuencia: {self.frecuencia_actual_ghz} GHz | Estado: {estado}")


def iniciar_bucle_termico(ciclos: int = 15):
    sgt = sistema_gestion_termica(t0_frio=60.0, t1_caliente=85.0)

    print("INICIANDO CONTROLADOR DE GESTION TERMICA (DVFS/THROTTLING)")
    print(f"Umbral de Alerta (T1): {sgt.t1_caliente} C")
    print(f"Umbral de Enfriamiento (T0): {sgt.t0_frio} C\n")

    for i in range(1, ciclos + 1):
        temp = sgt.leer_sensor_temperatura()
        print(f"[Paso {i:2d}/{ciclos}] ", end="")
        sgt.evaluar_politica_termica(temp)
        time.sleep(0.3)


if __name__ == "__main__":
    iniciar_bucle_termico(ciclos=15)