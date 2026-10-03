# CineMax - Cartelera y seleccion de funcion

from datos import cartelera
from utilidades import pedir_dia, buscar_funcion


def mostrar_cartelera(dia):
    print()
    print("Cartelera del", dia)
    print("-" * 70)
    print("Sala  Horario   Formato  Pelicula")
    print("-" * 70)
    # las ordeno por sala para que se vea mejor
    funciones = sorted(cartelera[dia], key=lambda x: x["sala"])
    for f in funciones:
        print(str(f["sala"]).ljust(6) + f["horario"].ljust(10) + f["formato"].ljust(9) + f["pelicula"])
    print("-" * 70)


def ver_cartelera():
    dia = pedir_dia()
    mostrar_cartelera(dia)


def pedir_funcion():
    # pide dia, sala y horario. Si algo esta mal devuelve None, None
    dia = pedir_dia()
    mostrar_cartelera(dia)

    sala = input("Numero de sala (1-5): ").strip()
    if not sala.isdigit() or int(sala) < 1 or int(sala) > 5:
        print("Esa sala no existe.")
        return None, None
    sala = int(sala)

    horario = input("Horario (ej: 4:30 pm): ")
    funcion = buscar_funcion(dia, sala, horario)
    if funcion == None:
        print("La sala", sala, "no tiene funcion a esa hora el", dia + ".")
        return None, None

    return dia, funcion