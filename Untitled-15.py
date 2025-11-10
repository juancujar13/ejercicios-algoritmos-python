x = float(input("Ingrese el número x: "))
minimo_valor = float(input("Ingrese el límite inferior (minimoValor): "))
maximo_valor = float(input("Ingrese el límite superior (maximoValor): "))
if x >= minimo_valor and x <= maximo_valor:
    print(f"El valor {x} está DENTRO del intervalo [{minimo_valor}, {maximo_valor}].")
else:
    print(f"El valor {x} está FUERA del intervalo [{minimo_valor}, {maximo_valor}].")