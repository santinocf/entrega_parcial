def cargar_pacientes(pacientes):
    n = int(input("Ingrese la cantidad de pacientes que desea cargar: "))
    for _ in range(n):
        numero_historia_clinica = int(
            input("Ingrese el numero de Historia Clinica del paciente:")
        )
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        edad_paciente = int(input("Ingrese la edad del paciente: "))
        diagnostico_paciente = input("Ingrese el diagnostico del paciente:")
        cantidad_dias = int(input("Ingrese la cantidad de dias internado: "))
        pacientes.append(
            [
                numero_historia_clinica,
                nombre_paciente,
                edad_paciente,
                diagnostico_paciente,
                cantidad_dias,
            ]
        )


def buscar_paciente(pacientes, numero_historia_clinica):
    for paciente in pacientes:
        if paciente[0] == numero_historia_clinica:
            print(
                f"Paciente encontrado: Número de H.C: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Cantidad de días internado: {paciente[4]}"
            )
            return
    print("Paciente no encontrado.")


def ordenar_pacientes(pacientes):
    for i in range(len(pacientes)):
        for j in range(0, len(pacientes) - i - 1):
            if (
                pacientes[j][0] > pacientes[j + 1][0]
            ):  # #Comparamos los números de historia clínica
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]

    print("Pacientes ordenados por número de Historia Clínica de forma ascendente:")
    for paciente in pacientes:
        print(
            f"Número de H.C: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Cantidad de días internado: {paciente[4]}"
        )


# Función para calcular el promedio de días de internación
def promedio_dias_internacion(pacientes):
    if not pacientes:
        print("No hay pacientes en la lista.")
        return
    total_dias = 0
    for paciente in pacientes:
        total_dias += paciente[4]  # Sumar los días de internación
    promedio = total_dias / len(pacientes)  # Calcular el promedio
    print(
        f"El promedio de días de internación de todos los pacientes es: {promedio:.2f} días."
    )
