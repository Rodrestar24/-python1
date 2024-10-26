
nombre =input("Introduce tu nombre: ")

nombre_mayusculas = nombre.upper()

numero_caracteres = len(nombre)

print( "Nombre en mayúsculas:"+ nombre_mayusculas)
print ("Número de caracteres:"+ numero_caracteres)

for _ in range(numero_caracteres):
    print (nombre)
