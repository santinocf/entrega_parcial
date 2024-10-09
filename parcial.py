from funcionesParcial import cargar_pacientes,mostrar_pacientes,buscar_paciente, ordenar_pacientes,mostrar_max_paciente,mostrar_min_paciente,paciente_mas_5_dias_internados,promedio_dias_internacion
def menu():
    pacientes = []
    salir = ""

    while salir != "salir":
        print("""\nSistema de Gestión de Clínica
                1. Cargar pacientes
                2. Mostrar todos los pacientes 
                3. Buscar pacientes por número de Historia Clinica
                4. Ordenar pacientes por número de Historia Clinica
                5. Mostrar paciente con más días de internación
                6. Mostrar paciente con menos días de internación
                7. Cantidad de pacientes con más de 5 días de internación
                8. Promedio de días de internación de todos los pacientes
                9. Salir""")
        opcion = input("Seleccione una opcion: ")
        
        
        if opcion == "1":
            cargar_pacientes(pacientes)
        elif opcion=="2":
            mostrar_pacientes(pacientes)
        elif opcion =="3":
            numero_historia_clinica = int(input("Ingrese el número de historia clínica que desea buscar: "))
            buscar_paciente(pacientes, numero_historia_clinica)
        elif opcion =="4":
            ordenar_pacientes(pacientes)
        elif opcion =="5":
            mostrar_max_paciente(pacientes)    
        elif opcion =="6":
            mostrar_min_paciente(pacientes)
        elif opcion =="7":
            paciente_mas_5_dias_internados(pacientes)
        elif opcion =="8":
            promedio_dias_internacion(pacientes)
        elif opcion =="9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, intente de nuevo.")

menu()