import random

def jugar_adivinanza():
    print("\n--- ¡ADIVINA EL NÚMERO! ---")
    
    # Configuramos el rango
    inicio = 1
    fin = 100
    numero_secreto = random.randint(inicio, fin)
    intentos = 0
    adivinado = False

    print(f"He pensado un número entre {inicio} y {fin}.")
    print("¿Puedes adivinar cuál es?")

    while not adivinado:
        try:
            # Pedimos el número al usuario
            intento_usuario = int(input("\nIntroduce tu número: "))
            intentos += 1

            # Lógica de comparación
            if intento_usuario < numero_secreto:
                print("Demasiado bajo. ¡Prueba más alto!")
            elif intento_usuario > numero_secreto:
                print("Demasiado alto. ¡Prueba más bajo!")
            else:
                adivinado = True
                print(f"\n¡FELICIDADES! Has acertado el número {numero_secreto}.")
                print(f"Te ha tomado {intentos} intentos.")
        
        except ValueError:
            print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    jugar_adivinanza()
