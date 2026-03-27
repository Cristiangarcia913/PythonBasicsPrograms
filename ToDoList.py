def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Borrar tarea")
    print("4. Salir")

def ejecutar_programa():
    tareas = []  # Aquí se guardarán los textos
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        # 1. VER TAREAS
        if opcion == "1":
            print("\n--- LISTA DE TAREAS ---")
            if not tareas:
                print("La lista está vacía.")
            else:
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")

        # 2. AÑADIR TAREA
        elif opcion == "2":
            nueva_tarea = input("Escribe la tarea: ")
            tareas.append(nueva_tarea)
            print("¡Tarea añadida con éxito!")

        # 3. BORRAR TAREA
        elif opcion == "3":
            if not tareas:
                print("No hay nada que borrar.")
            else:
                try:
                    # Mostramos las tareas para que el usuario sepa cuál elegir
                    for i, tarea in enumerate(tareas, 1):
                        print(f"{i}. {tarea}")
                    
                    indice = int(input("Introduce el número de la tarea a eliminar: "))
                    # Restamos 1 porque las listas en Python empiezan en 0
                    tarea_eliminada = tareas.pop(indice - 1)
                    print(f"Eliminada: '{tarea_eliminada}'")
                except (ValueError, IndexError):
                    print("Error: Introduce un número de la lista válido.")

        # 4. SALIR
        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_programa()
