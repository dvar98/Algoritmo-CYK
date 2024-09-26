import time

def cyk_algorithm(grammar, string):
    n = len(string)
    r = len(grammar)  # Número de reglas en la gramática

    # Crear tabla CYK con dimensiones n x n
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Llenar la tabla para las subcadenas de longitud 1
    for i, symbol in enumerate(string):
        for lhs, rhs in grammar:
            if rhs == [symbol]:
                table[i][i].add(lhs)

    # Llenar la tabla para subcadenas de longitud 2 a n
    for l in range(2, n+1):  # Longitud de la subcadena
        for i in range(n-l+1):
            j = i + l - 1
            for k in range(i, j):
                for lhs, rhs in grammar:
                    if len(rhs) == 2 and rhs[0] in table[i][k] and rhs[1] in table[k+1][j]:
                        table[i][j].add(lhs)

    # Verificar si el símbolo inicial está en la última celda
    return 'S' in table[0][n-1]

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

# Cadena de prueba
string = "baaba"

# Medir el tiempo de ejecución
start_time = time.time()
result = cyk_algorithm(grammar, string)
end_time = time.time()

print(f"Resultado: {result}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
