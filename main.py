# Importamos funciones a este archivo desde (from) funcionesMostrar y funcionesPacientes
from funcionesMostrar import (
    mostrar_pacientes,
    mostrar_max_paciente,
    mostrar_min_paciente,
    paciente_mas_5_dias_internados,
)
from funcionesPacientes import (
    cargar_pacientes,
    buscar_paciente,
    ordenar_pacientes,
    promedio_dias_internacion,
)


def menu():  # Muestra el menú principal del sistema de gestión de pacientes de la clínica

    pacientes = []
    salir = ""

    while (
        salir != "salir"
    ):  # El bucle principal continúa ejecutándose hasta que el usuario elige salir.
        print(
            """\nSistema de Gestión de Clínica
                1. Cargar pacientes
                2. Mostrar todos los pacientes 
                3. Buscar pacientes por número de Historia Clinica
                4. Ordenar pacientes por número de Historia Clinica
                5. Mostrar paciente con más días de internación
                6. Mostrar paciente con menos días de internación
                7. Cantidad de pacientes con más de 5 días de internación
                8. Promedio de días de internación de todos los pacientes
                9. Salir"""
        )
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cargar_pacientes(pacientes)  # Carga pacientes en la lista
        elif opcion == "2":
            # Validación de lista vacía
            if pacientes:
                mostrar_pacientes(pacientes)  # Muestra todos los pacientes
            else:
                print(
                    "No hay pacientes para mostrar."
                )  # Mensaje si la lista está vacía
        elif opcion == "3":  # Busca paciente por número de historia clinica
            numero_historia_clinica = int(
                input("Ingrese el número de historia clínica que desea buscar: ")
            )
            buscar_paciente(pacientes, numero_historia_clinica)
        elif opcion == "4":
            # Validación de lista vacía antes de ordenar
            if pacientes:
                ordenar_pacientes(pacientes)  # Ordena la lista de pacientes
            else:
                print(
                    "No hay pacientes para ordenar."
                )  # Mensaje si la lista está vacía
        elif opcion == "5":
            # Validación de lista vacía antes de mostrar paciente con más días
            if pacientes:
                mostrar_max_paciente(
                    pacientes
                )  # Muestra paciente con más días de internación
            else:
                print(
                    "No hay pacientes para mostrar."
                )  # Mensaje si la lista está vacía
        elif opcion == "6":
            # Validación de lista vacía antes de mostrar paciente con menos días
            if pacientes:
                mostrar_min_paciente(
                    pacientes
                )  # Muestra paciente con menos días de internación
            else:
                print(
                    "No hay pacientes para mostrar."
                )  # Mensaje si la lista está vacía
        elif opcion == "7":
            paciente_mas_5_dias_internados(
                pacientes
            )  # Cuenta pacientes con más de 5 días
        elif opcion == "8":
            promedio_dias_internacion(
                pacientes
            )  # Calcula el promedio de días de internación
        elif opcion == "9":
            print("Saliendo del sistema...")  # Mensaje de salida
            break
        else:
            print(
                "Opcion no valida, intente de nuevo."
            )  # Mensaje de error para entradas no válidas


menu()  # Llama a la función para ejecutar el menú
