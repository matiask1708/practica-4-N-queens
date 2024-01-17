
import time
import matplotlib.pyplot as plt

def solución_valida(fila, col, queens):
    for f in range(fila):
        if col == queens[f]:
            return False
        elif abs(col - queens[f]) == abs(fila -f ):
            return False
    return True 
def tiempo():
    inicio = time.time()
    return time.time() - inicio

def n_queens(n):
    queens = [' '] * n
    resultado = colocar_queen(0, queens, n)
    print(f"El número total de soluciones para el problema de las N reinas mediante backtracking con {n} reinas es: {resultado}")

def imprimir_tablero(tablero):
    n = len(tablero)
    for fila in range(n):
        for col in range(n):
            if tablero[fila] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def colocar_queen(fila, queens, n):
    if fila == n:
        imprimir_tablero(queens)
        return 1
    else:
        solucion_total = 0
        for col in range(n):
            if solución_valida(fila, col, queens):
                queens[fila] = col
                solucion_total += colocar_queen(fila + 1, queens, n)
        return solucion_total

def poda(fila, queens, n):
    if fila == n:
        imprimir_tablero(queens)
        return 1
    else:
        sol = 0
        for col in range(n):
            if solución_valida(fila, col, queens):
                queens[fila] = col
                if fila == 0 or (fila > 0 and solución_valida(fila, col, queens)):
                    sol += poda(fila + 1, queens, n)
                queens[fila] = -1
    return sol

def n_queens_poda(n):
    queens = [-1] * n
    resultado = poda(0, queens, n)
    print(f"El número total de soluciones para el problema de las N reinas mediante poda con {n} reinas es: {resultado}")

def heuristica(fila, queens, n):
    for col in range(n):
        if solución_valida(fila, col, queens):
            return col
    return None

def colocar_queen_heuristica(fila, queens, n):
    if fila == n:
        imprimir_tablero(queens)
        return 1
    else:
        solucion_total = 0
        posicion_valida = heuristica(fila, queens, n)
        if posicion_valida is not None:
            queens[fila] = posicion_valida
            solucion_total += colocar_queen_heuristica(fila + 1, queens, n)
            queens[fila] = ' '
        return solucion_total

def n_queens_heuristica(n):
    queens = [' '] * n
    resultado = colocar_queen_heuristica(0, queens, n)
    print(f"El número total de soluciones para el problema de las N reinas mediante heurísticas inteligentes con {n} reinas es: {resultado}")

def medir_tiempo(tam, estrategia):
    tiempos = []
    for n in tam:
        inicio = time.time()
        if estrategia == "backtracking":
            n_queens(n)
        elif estrategia == "poda":
            n_queens_poda(n)
        elif estrategia == "heuristica":
            n_queens_heuristica(n)
        else:
            raise ValueError("Estrategia no válida")
        tiempo_ejecucion = time.time() - inicio
        tiempos.append(tiempo_ejecucion)
    return tiempos

def crear_grafica(tamano_problema, tiempos, estrategia):
    plt.plot(tamano_problema, tiempos, label=estrategia)
    plt.xlabel('Tamaño del problema (N)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempo de ejecución en función del tamaño del problema')
    plt.legend()
    plt.show()

# Prueba con N desde 1 hasta 10
tamano_problema = list(range(1, 10))

# Medir tiempo de ejecución para la versión básica
tiempos_backtracking = medir_tiempo(tamano_problema, "backtracking")
crear_grafica(tamano_problema, tiempos_backtracking, "Backtracking")
# Medir tiempo de ejecución para la versión con poda por conflicto
tiempos_poda = medir_tiempo(tamano_problema, "poda")
crear_grafica(tamano_problema, tiempos_poda, "Poda ")

# Medir tiempo de ejecución para la versión con heurística
tiempos_heuristica = medir_tiempo(tamano_problema, "heuristica")
crear_grafica(tamano_problema, tiempos_heuristica, "Heurística")
