# CineMax - Funciones de ayuda (las usan varios modulos)

from datos import dias, cartelera, LETRAS, COLUMNAS


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