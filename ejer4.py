import heapq
import time

print("INICIANDO CONTROLADOR DE INTERRUPCIONES (PIC)")

class controlador_interrupciones:
    def __init__(self):
        self.cola_prioridad = []
        self.contador = 0

    def activar_interrupcion(self, prioridad: int, nombre: str, descripcion: str):
        self.contador += 1
        heapq.heappush(self.cola_prioridad, (prioridad, self.contador, nombre, descripcion))
        print(f"[HW SIGNAL] -> IRQ Recibida: '{nombre}' (Prioridad Nivel {prioridad})")

    def atender_interrupciones(self):
        print("\n INICIANDO ATENCION DE INTERRUPCIONES (ISR) ")
        while self.cola_prioridad:
            prioridad, _, nombre, descripcion = heapq.heappop(self.cola_prioridad)
            print(f"[CPU ISR] Atendiendo: {nombre:20s} | Prioridad: {prioridad} | Detalle: {descripcion}")
            time.sleep(0.3)
        print(" TODAS LAS INTERRUPCIONES FUERON ATENDIDAS \n")

pic = controlador_interrupciones()

print("Simulando llegada de eventos heterogeneos en el bus.\n")

pic.activar_interrupcion(prioridad=3, nombre="TECLADO_KEYPRESS", descripcion="Tecla ENTER presionada")
pic.activar_interrupcion(prioridad=5, nombre="PUERTO_SERIE_PAQUETE", descripcion="Byte recibido en UART")
pic.activar_interrupcion(prioridad=0, nombre="POWER_FAIL_NMI", descripcion="Bajada de tension critica detectada")
pic.activar_interrupcion(prioridad=1, nombre="SYSTEM_TIMER", descripcion="Tick de reloj del SO (10ms)")
pic.activar_interrupcion(prioridad=3, nombre="MOUSE_MOVE", descripcion="Movimiento en eje X/Y")

pic.atender_interrupciones()