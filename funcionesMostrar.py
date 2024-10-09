def mostrar_pacientes(pacientes):
    print("Lista de Pacientes:")
    for paciente in pacientes:
        print(
            f"Número de H.C: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]},Diagnóstico: {paciente[3]}, Cantidad de días internado: {paciente[4]}"
        )


def mostrar_max_paciente(pacientes):
    if not pacientes:
        print("No hay pacientes en la lista.")
        return
    max_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > max_paciente[4]:  # Comparar días de internación
            max_paciente = paciente
    print(
        f"Paciente con más días de internación: Número de H.C: {max_paciente[0]}, Nombre: {max_paciente[1]},Edad: {max_paciente[2]}, Diagnóstico: {max_paciente[3]}, Cantidad de días internado: {max_paciente[4]}"
    )


def mostrar_min_paciente(pacientes):
    if not pacientes:
        print("No hay pacientes en la lista.")
        return
    min_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < min_paciente[4]:  # Comparar días de internación
            min_paciente = paciente
    print(
        f"Paciente con menos días de internación: Número de H.C: {min_paciente[0]}, Nombre: {min_paciente[1]},Edad: {min_paciente[2]}, Diagnóstico: {min_paciente[3]}, Cantidad de días internado: {min_paciente[4]}"
    )


def paciente_mas_5_dias_internados(pacientes):
    encontrados = False
    for paciente in pacientes:
        if paciente[4] > 5:
            print(
                f"Paciente con mas de 5 días de internación: Número de H.C: {paciente[0]}, Nombre: {paciente[1]},Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Cantidad de días internado: {paciente[4]}"
            )
            encontrados = True
    if not encontrados:
        print("No hay pacientes con más de 5 días de internación.")
