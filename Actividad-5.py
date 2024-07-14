contador = 0
acumulador = 0
while contador < 5:
    numero = int(input("Ingrese un numero: "))
    acumulador += numero

    contador += 1
print("La suma acumulada es de:", acumulador)
promedio = acumulador / contador
print("El promedio es de:", promedio)
