# Algoritmo CYK - Análisis de Complejidad

Este repositorio contiene una implementación del **algoritmo CYK** en Python para determinar si una cadena pertenece al lenguaje definido por una gramática libre de contexto en forma normal de Chomsky.

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
