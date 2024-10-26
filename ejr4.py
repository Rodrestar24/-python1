 
peso = float(input("Peso en kg: "))
estatura = float(input("Estatura en metros: "))

imc = peso / (estatura ** 2)

print("Tu índice de masa corporal es", round(imc, 2))
