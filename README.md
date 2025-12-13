# Encapsulamiento-funcional

El encapsulamiento funcional se logra al aislar la lógica interna del programa dentro de un módulo, mientras que el archivo __init__.py actúa como interfaz pública, exponiendo únicamente las funciones necesarias para el usuario. De esta forma, se ocultan los detalles de implementación y se facilita el uso del paquete.

## Funciones Disponibles

- adelante(n)
Dibuja el movimiento horizontal de la tortuga hacia la derecha por n pasos.

- abajo(n)
Dibuja el movimiento vertical hacia abajo manteniendo la posición horizontal acumulada.

- reiniciar()
Reinicia la posición horizontal de la tortuga al valor inicial.

## Objetivo del Proyecto

- Comprender el concepto de encapsulamiento

- Aplicar modularización del código

- Separar la lógica del programa de su interfaz

- Facilitar la reutilización de funciones

- Practicar el uso de paquetes en Python

  ## Estructura aplicada

``` python
  Encapsulamiento-funcional/
│
├── main.py
└── paquete/
    ├── __init__.py
    └── logic.py
```


