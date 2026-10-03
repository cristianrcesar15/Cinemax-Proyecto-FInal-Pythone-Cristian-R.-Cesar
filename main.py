# CineMax - Sistema de reservas
# Archivo principal: aqui esta el menu

from datos import crear_asientos
from peliculas import ver_cartelera
from salas import mostrar_asientos, ver_disponibilidad
from reservaciones import reservar, cancelar


def menu():
    crear_asientos()
    while True:
        print()
        print("==============================")
        print("      CINEMAX - RESERVAS")
        print("==============================")
        print("1. Ver cartelera de un dia")
        print("2. Mostrar asientos")
        print("3. Reservar asiento")
        print("4. Cancelar reserva")
        print("5. Ver disponibilidad")
        print("6. Salir")
        opcion = input("Opcion: ").strip()

        if opcion == "1":
            ver_cartelera()
        elif opcion == "2":
            mostrar_asientos()
        elif opcion == "3":
            reservar()
        elif opcion == "4":
            cancelar()
        elif opcion == "5":
            ver_disponibilidad()
        elif opcion == "6":
            print("Gracias por usar CineMax!")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
    
