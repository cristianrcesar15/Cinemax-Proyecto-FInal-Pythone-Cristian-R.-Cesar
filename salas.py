# CineMax - Mostrar asientos y disponibilidad

from datos import asientos, cartelera, FILAS, COLUMNAS, LETRAS
from utilidades import pedir_dia
from peliculas import pedir_funcion


def imprimir_asientos(dia, funcion):
    matriz = asientos[(dia, funcion["sala"])]
    print()
    print(funcion["pelicula"], "-", funcion["formato"])
    print(dia, funcion["horario"], "- Sala", funcion["sala"])
    print()
    print("      [ PANTALLA ]")
    print()

    linea = "   "
    for c in range(COLUMNAS):
        linea = linea + str(c + 1) + "  "
    print(linea)

    for f in range(FILAS):
        linea = LETRAS[f] + "  "
        for c in range(COLUMNAS):
            linea = linea + matriz[f][c] + "  "
        print(linea)

    print()
    print("  . = libre    X = ocupado")


def mostrar_asientos():
    dia, funcion = pedir_funcion()
    if funcion == None:
        return
    imprimir_asientos(dia, funcion)


def contar_asientos(dia, sala):
    libres = 0
    ocupados = 0
    for fila in asientos[(dia, sala)]:
        for a in fila:
            if a == ".":
                libres += 1
            else:
                ocupados += 1
    return libres, ocupados


def ver_disponibilidad():
    dia = pedir_dia()
    total = FILAS * COLUMNAS
    print()
    print("Disponibilidad del", dia)
    print("-" * 78)
    print("Sala  Horario   Libres  Ocupados  % Ocup.  Pelicula")
    print("-" * 78)
    funciones = sorted(cartelera[dia], key=lambda x: x["sala"])
    for f in funciones:
        libres, ocupados = contar_asientos(dia, f["sala"])
        porc = ocupados * 100 / total
        linea = str(f["sala"]).ljust(6) + f["horario"].ljust(10)
        linea = linea + str(libres).ljust(8) + str(ocupados).ljust(10)
        linea = linea + (str(round(porc, 1)) + "%").ljust(9) + f["pelicula"] + " (" + f["formato"] + ")"
        print(linea)
    print("-" * 78)