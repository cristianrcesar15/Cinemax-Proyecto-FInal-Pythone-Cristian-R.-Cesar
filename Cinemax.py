# CineMax - Sistema de reservas
# 5 salas, cartelera de una semana

# 1. DATOS GENERALES

FILAS = 5
COLUMNAS = 6
LETRAS = "ABCDE"

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# 2. CARTELERA DE LA SEMANA

cartelera = {
    "Lunes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "2:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "4:30 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 3, "horario": "6:00 pm", "formato": "4DX"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "5:30 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 5, "horario": "8:00 pm", "formato": "CXC"},
    ],
    "Martes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "5:00 pm", "formato": "4DX"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 1, "horario": "7:00 pm", "formato": "Normal"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 5, "horario": "6:30 pm", "formato": "3D"},
        {"pelicula": "El Final", "sala": 4, "horario": "9:00 pm", "formato": "Normal"},
    ],
    "Miércoles": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "2:30 pm", "formato": "CXC"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 1, "horario": "7:30 pm", "formato": "3D"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 2, "horario": "5:00 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 3, "horario": "8:30 pm", "formato": "4DX"},
    ],
    "Jueves": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 2, "horario": "6:30 pm", "formato": "3D"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 3, "horario": "3:30 pm", "formato": "Normal"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 4, "horario": "8:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "2:00 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 5, "horario": "5:30 pm", "formato": "CXC"},
    ],
    "Viernes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 5, "horario": "4:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 4, "horario": "7:00 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 1, "horario": "5:30 pm", "formato": "CXC"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 3, "horario": "9:00 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 2, "horario": "2:30 pm", "formato": "4DX"},
    ],
    "Sábado": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "6:00 pm", "formato": "4DX"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 5, "horario": "8:30 pm", "formato": "3D"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "4:30 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 3, "horario": "7:30 pm", "formato": "CXC"},
    ],
    "Domingo": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "2:30 pm", "formato": "3D"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "5:00 pm", "formato": "Normal"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "7:00 pm", "formato": "CXC"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "8:30 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
    ],
}

# 3. ESTRUCTURA DE DATOS (Esto son los asientos de cada sala)

# asientos de cada funcion. La clave es (dia, sala) porque cada sala
# solo tiene una funcion por dia
asientos = {}

# quien reservo cada asiento -> (dia, sala, "C3"): nombre
reservas = {}


def crear_asientos():
    for dia in dias:
        for sala in range(1, 6):
            matriz = []
            for f in range(FILAS):
                fila = []
                for c in range(COLUMNAS):
                    fila.append(".")
                matriz.append(fila)
            asientos[(dia, sala)] = matriz

# FUNCIONES DE AYUDA (las usan varias opciones del menu)

def quitar_tildes(texto):
    texto = texto.lower().strip()
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i")
    texto = texto.replace("ó", "o").replace("ú", "u")
    return texto


def pedir_dia():
    print()
    for i in range(len(dias)):
        print(" ", i + 1, "-", dias[i])
    while True:
        op = input("Elige el dia (numero o nombre): ").strip()
        if op.isdigit():
            n = int(op)
            if n >= 1 and n <= 7:
                return dias[n - 1]
        else:
            # por si lo escriben sin tilde o en minuscula
            for d in dias:
                if quitar_tildes(d) == quitar_tildes(op):
                    return d
        print("Ese dia no existe, intenta de nuevo.")


def buscar_funcion(dia, sala, horario):
    # devuelve la funcion si esa sala tiene funcion a esa hora ese dia
    for f in cartelera[dia]:
        if f["sala"] == sala:
            h1 = f["horario"].replace(" ", "").lower()
            h2 = horario.replace(" ", "").lower()
            if h1 == h2:
                return f
    return None


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


def convertir_asiento(texto):
    # convierte "C3" en (2, 2). Si no es valido devuelve None
    texto = texto.strip().upper()
    if len(texto) != 2:
        return None
    letra = texto[0]
    numero = texto[1]
    if letra not in LETRAS or not numero.isdigit():
        return None
    col = int(numero) - 1
    if col < 0 or col >= COLUMNAS:
        return None
    fila = LETRAS.index(letra)
    return fila, col

# 4.1 VER CARTELERA DE UN DIA

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

# 4.2 MOSTRAR ASIENTOS

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

# 4.3 RESERVAR ASIENTO

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

# 4.4 CANCELAR RESERVA

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

# 4.5 VER DISPONIBILIDAD

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

# 5. MENU PRINCIPAL

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


menu()
