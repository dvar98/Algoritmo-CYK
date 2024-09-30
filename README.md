# Algoritmo CYK - Análisis de Complejidad

Este repositorio contiene una implementación del **algoritmo CYK** en Python para determinar si una cadena pertenece al lenguaje definido por una gramática libre de contexto en forma normal de Chomsky.

# Gráfica que representa el crecimiento del **algoritmo CYK**

![{05E607C0-09D3-4B75-9832-4C2C29EE82E2}](https://github.com/user-attachments/assets/f3b043f1-4b2e-4025-a448-b397d4c5d740)

la gráfica que muestra el crecimiento cúbico del tiempo de ejecución del algoritmo CYK, representado por la función 
𝑂
(
𝑛
3
).
Como se puede observar, a medida que la longitud de la cadena de entrada 
𝑛
aumenta, el número de operaciones crece de manera rápida, destacando la naturaleza cúbica del algoritmo.

# Demostración matematica

El algoritmo CYK es un método eficiente para determinar si una cadena pertenece a un lenguaje generado por una gramática libre de contexto en forma normal de Chomsky (CNF).

## Descripción

1. **Gramática en CNF**: La gramática debe tener reglas de la forma:
   - \( A → BC \)
   - \( A → a \)

2. **Matriz \( T \)**: Utiliza una matriz triangular \( T[i,j] \) donde cada entrada contiene las variables que generan el substring \( w_i, ..., w_j \).

## Procedimiento

- **Base**: Para substrings de longitud 1:
  \[
  T[i,i] = \{A ∣ A → w_i\}
  \]

- **Caso recursivo**: Para substrings de longitud \( > 1 \):
  \[
  T[i,j] = T[i,j] ∪ \{A ∣ A → BC, B ∈ T[i,k], C ∈ T[k+1,j]\}
  \]

## Verificación

La cadena \( w \) es aceptada si \( S ∈ T[1,n] \), donde \( S \) es el símbolo inicial de la gramática.

## Complejidad

La complejidad temporal es \( O(n^3 ⋅ |G|) \), donde \( n \) es la longitud de la cadena y \( |G| \) es el tamaño de la gramática.



## Implementación

El archivo `cyk_algorithm.py` contiene la implementación del algoritmo CYK. La gramática utilizada incluye producciones terminales y no terminales, y puede probar diferentes cadenas y gramáticas.

## Instalación y ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/
   cd cyk-algorithm

2. Ejecuta el algoritmo:
   ```bash
   python3 cyk.py

## Pruebas de complejidad

Este proyecto incluye diferentes pruebas para evaluar la complejidad del algoritmo desde varias perspectivas: temporal, espacial, I/O, paralelización y más.

### 1. Complejidad Temporal

La complejidad temporal del algoritmo CYK es $O(n^3 \cdot |G|)$, donde $n$ es la longitud de la cadena y $|G|$ es el número de reglas en la gramática.

Midamos el tiempo de ejecución usando la herramienta `time`:

```bash
time python3 cyk.py
```

El comando `time` te proporcionará tres valores importantes:

- **real**: Tiempo total transcurrido desde que se inició hasta que se completó la ejecución del programa.
- **user**: Tiempo de CPU utilizado en modo usuario, que incluye las operaciones realizadas por el programa que no requieren interacción con el núcleo del sistema operativo.
- **sys**: Tiempo de CPU utilizado en modo sistema, que se refiere al tiempo que el núcleo del sistema operativo pasó ejecutando tareas en nombre del programa.

### 2. Complejidad Espacial (Uso de memoria)

La complejidad espacial del algoritmo CYK es **O(n²)**, ya que utiliza una tabla de **n × n** para almacenar los resultados intermedios.

Para obtener el uso máximo de memoria durante la ejecución, puedes usar el comando `time -v`:

```bash
/usr/bin/time -v python3 cyk_algorithm.py
```
El resultado te mostrará el "Maximum resident set size", que es la memoria máxima utilizada (en kilobytes).
