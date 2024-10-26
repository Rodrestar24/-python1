#Ejr5
import random

numero1 = random.randint(2, 10)
numero2 = random.randint(2, 10)

respuesta_correcta = numero1 * numero2

respuesta_usuario = int(input("¿Cuál es el resultado de " + numero1 + " * " + numero2 + "? "))
if respuesta_usuario == respuesta_correcta:
    print("¡Correcto!")
else:
    print("No es correcta. La respuesta correcta es", respuesta_correcta)
