posicion_x = 0

def adelante(n):
    global posicion_x
    print(" " * posicion_x + "-" * n + "🐢")
    posicion_x += n

def abajo(n):
    for _ in range(n):
        print(" " * posicion_x + "|")

def reiniciar():
    global posicion_x
    posicion_x = 0
    print("\nPosición reiniciada a 0\n")





