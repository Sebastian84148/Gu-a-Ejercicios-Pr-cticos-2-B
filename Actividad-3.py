numero = int(input("Ingrese un numero: "))
while numero < 0 or numero > 9:
    print("Numero incorrecto. Vuelva a intentarlo")
    numero = int(input("Ingrese un numero: "))
print("Numero correcto")