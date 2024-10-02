import time
import matplotlib.pyplot as plt

def cyk_algorithm(grammar, string):
    n = len(string)

    # Crear tabla CYK con dimensiones n x n
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Llenar la tabla para las subcadenas de longitud 1
    for i, symbol in enumerate(string):
        for lhs, rhs in grammar:
            if rhs == [symbol]:
                table[i][i].add(lhs)

    # Llenar la tabla para subcadenas de longitud 2 a n
    for l in range(2, n + 1):  # Longitud de la subcadena
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for lhs, rhs in grammar:
                    if len(rhs) == 2 and rhs[0] in table[i][k] and rhs[1] in table[k + 1][j]:
                        table[i][j].add(lhs)

    # Verificar si el símbolo inicial está en la última celda
    return 'S' in table[0][n - 1]

# Ejemplo de gramática en CNF
grammar = [
    ('S', ['A', 'B']),
    ('S', ['B', 'C']),
    ('A', ['B', 'A']),
    ('A', ['a']),
    ('B', ['C', 'C']),
    ('B', ['b']),
    ('C', ['A', 'B']),
    ('C', ['a']),
]

# Lista de cadenas de prueba de diferentes tamaños
strings = ["b", "ba", "baa", "baaa", "baaba", "baabaab", "baabaabaa", "baabaabaaa"]
execution_times = []

# Medir el tiempo de ejecución para cada cadena
for string in strings:
    start_time = time.time()
    result = cyk_algorithm(grammar, string)
    end_time = time.time()
    execution_times.append(end_time - start_time)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(strings, execution_times, marker='o')
plt.title('Tiempo de ejecución del algoritmo CYK')
plt.xlabel('Cadenas de entrada')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.xticks(rotation=45)
plt.grid()
plt.show()
