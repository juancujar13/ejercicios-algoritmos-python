primos_hasta_20 = [2, 3, 5, 7, 11, 13, 17, 19]
numero = int(input("Ingrese un número entero entre 0 y 20: "))
if 0 <= numero <= 20:
    if numero in primos_hasta_20:
        print(f"El número {numero} SÍ es un número primo.")
    else:
        print(f"El número {numero} NO es un número primo.")    
else:
    print(f"Error: El número {numero} está fuera del rango solicitado (0-20).")