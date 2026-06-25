import csv

# -------------------------------
# Cargar empleados desde el CSV
# -------------------------------

empleados = {}

with open(r"C:\Users\karen\OneDrive\Escritorio\AGUIRRE FACU\OE\Chatbot_Vacaciones\empleados.csv",
          mode="r",
          encoding="latin-1") as archivo:
    lector = csv.DictReader(archivo, delimiter=";")

    print("Columnas encontradas:")
    print(lector.fieldnames)

    for fila in lector:
        empleados[fila["Legajo"]] = {
            "nombre": fila["Nombre"],
            "dias": int(fila["Dias_Disponibles"])
        }

# -------------------------------
# Máquina de Estados
# -------------------------------

ESTADO_LEGAJO = 0
ESTADO_DIAS = 1
ESTADO_FIN = 2

estado = ESTADO_LEGAJO

print("====================================")
print(" CHATBOT - SOLICITUD DE VACACIONES")
print("====================================")

while estado != ESTADO_FIN:

    # ---------------- Estado 0 ----------------

    if estado == ESTADO_LEGAJO:

        legajo = input("\nIngrese su legajo: ")

        if legajo not in empleados:
            print("Legajo inexistente.")
            continue

        empleado = empleados[legajo]

        print(f"\nBienvenido {empleado['nombre']}")
        print(f"Días disponibles: {empleado['dias']}")

        estado = ESTADO_DIAS

    # ---------------- Estado 1 ----------------

    elif estado == ESTADO_DIAS:

        dias = input("\n¿Cuántos días desea solicitar?: ")

        # Camino infeliz

        if not dias.isdigit():
            print("Error, por favor ingresá un número válido.")
            continue

        dias = int(dias)

        if dias <= 0:
            print("Debe ingresar un número mayor que cero.")
            continue

        if dias > empleado["dias"]:

            print("\nSolicitud rechazada.")
            print("No posee días suficientes.")

        else:

            empleado["dias"] -= dias

            print("\nSolicitud aprobada.")
            print("Vacaciones registradas correctamente.")
            print("Días restantes:", empleado["dias"])

        estado = ESTADO_FIN

print("\nGracias por utilizar el Chatbot.")