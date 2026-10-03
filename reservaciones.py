# CineMax - Reservar y cancelar

from datos import asientos, reservas
from utilidades import convertir_asiento
from peliculas import pedir_funcion
from salas import imprimir_asientos


def reservar():
    dia, funcion = pedir_funcion()
    if funcion == None:
        return
    sala = funcion["sala"]
    imprimir_asientos(dia, funcion)

    asiento = input("Asiento que quieres reservar (ej: C3): ").strip().upper()
    pos = convertir_asiento(asiento)
    if pos == None:
        print("Ese asiento no existe. Las filas van de A a E y las columnas de 1 a 6.")
        return
    fila, col = pos

    if asientos[(dia, sala)][fila][col] == "X":
        print("El asiento", asiento, "ya esta ocupado, elige otro.")
        return

    nombre = input("Nombre de quien reserva: ").strip()
    if nombre == "":
        nombre = "Sin nombre"

    asientos[(dia, sala)][fila][col] = "X"
    reservas[(dia, sala, asiento)] = nombre

    print()
    print("*** Reserva confirmada ***")
    print("Nombre:  ", nombre)
    print("Pelicula:", funcion["pelicula"])
    print("Formato: ", funcion["formato"])
    print("Dia:     ", dia, funcion["horario"])
    print("Sala:    ", sala)
    print("Asiento: ", asiento)


def cancelar():
    dia, funcion = pedir_funcion()
    if funcion == None:
        return
    sala = funcion["sala"]
    imprimir_asientos(dia, funcion)

    asiento = input("Asiento que quieres cancelar (ej: C3): ").strip().upper()
    pos = convertir_asiento(asiento)
    if pos == None:
        print("Ese asiento no existe.")
        return
    fila, col = pos

    if asientos[(dia, sala)][fila][col] == ".":
        print("El asiento", asiento, "no esta reservado, no hay nada que cancelar.")
        return

    nombre = reservas[(dia, sala, asiento)]
    asientos[(dia, sala)][fila][col] = "."
    del reservas[(dia, sala, asiento)]

    print()
    print("Reserva cancelada. El asiento", asiento, "que estaba a nombre de", nombre, "quedo libre.")