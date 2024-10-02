import time
from tabulate import tabulate


def cyk_algorithm(grammar, string):
    """
    Implementación del algoritmo CYK para verificar si una cadena pertenece a un lenguaje generado por una gramática en forma normal de Chomsky.

    Args:
        grammar (list): Gramática en forma normal de Chomsky, donde cada regla es una tupla (lhs, rhs) con lhs como símbolo no terminal y rhs como lista de símbolos terminales o no terminales.
        string (str): Cadena de entrada a verificar.

    Returns:
        list: Tabla CYK.
    """

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

    return table


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
table = cyk_algorithm(grammar, string)
end_time = time.time()


print("Tabla CYK:")
table_str = [["-" for _ in range(len(string))] for _ in range(len(string))]
for i in range(len(string)):
    for j in range(len(string)):
        if table[i][j]:
            table_str[i][j] = ", ".join(sorted(table[i][j]))
print(tabulate(table_str, tablefmt="grid"))


print("\nResultado:")
print(f"  La cadena '{string}' pertenece al lenguaje: {'S' in table[0][len(string)-1]}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")