from collections import deque

class Process:
    def __init__(self, pid: str, arrival_time: int, burst_time: int):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def simulate_round_robin(processes: list, quantum: int):
    processes.sort(key=lambda p: p.arrival_time)
    
    current_time = 0
    ready_queue = deque()
    completed_processes = []
    n = len(processes)
    visited = [False] * n

    print(f"--- INICIANDO PLANIFICADOR ROUND ROBIN (Quantum = {quantum} ms) ---")

    for i in range(n):
        if processes[i].arrival_time <= current_time:
            ready_queue.append(processes[i])
            visited[i] = True

    while ready_queue or any(p.remaining_time > 0 for p in processes):
        if not ready_queue:
            current_time += 1
            for i in range(n):
                if not visited[i] and processes[i].arrival_time <= current_time:
                    ready_queue.append(processes[i])
                    visited[i] = True
            continue

        current_process = ready_queue.popleft()
        
        execution_time = min(quantum, current_process.remaining_time)
        print(f"[t={current_time:2d}ms] Ejecutando {current_process.pid} durante {execution_time}ms...")

        current_time += execution_time
        current_process.remaining_time -= execution_time

        for i in range(n):
            if not visited[i] and processes[i].arrival_time <= current_time:
                ready_queue.append(processes[i])
                visited[i] = True

        if current_process.remaining_time > 0:
            ready_queue.append(current_process)
        else:
            current_process.completion_time = current_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed_processes.append(current_process)
            print(f"         └─> {current_process.pid} FINALIZADO a los {current_time}ms")

    print("\n================ RESULTADOS DE PLANIFICACIÓN ================")
    print(f"{'PID':<6}| {'Llegada':<8}| {'Rafaga':<8}| {'Fin':<6}| {'Turnaround':<12}| {'Espera':<8}")
    print("-" * 55)
    
    total_wait = 0
    total_turnaround = 0
    for p in completed_processes:
        total_wait += p.waiting_time
        total_turnaround += p.turnaround_time
        print(f"{p.pid:<6}| {p.arrival_time:<8}| {p.burst_time:<8}| {p.completion_time:<6}| {p.turnaround_time:<12}| {p.waiting_time:<8}")

    print("-" * 55)
    print(f"Tiempo Promedio de Espera:    {total_wait / n:.2f} ms")
    print(f"Tiempo Promedio de Resp/Ret:  {total_turnaround / n:.2f} ms")
    print("============================================================\n")


if __name__ == "__main__":
    procesos_lote = [
        Process(pid="P1", arrival_time=0, burst_time=5),
        Process(pid="P2", arrival_time=1, burst_time=3),
        Process(pid="P3", arrival_time=2, burst_time=8),
        Process(pid="P4", arrival_time=4, burst_time=2)
    ]

    QUANTUM_TIME = 2

    simulate_round_robin(procesos_lote, QUANTUM_TIME)