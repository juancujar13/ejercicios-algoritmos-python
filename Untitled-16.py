print("\n--- Ejercicio 7: Verificar número en tres intervalos abiertos ---")

x_intervalo = float(input("Ingrese el número x a verificar: "))

print("Defina el primer intervalo (abierto):")
min1 = float(input("  Límite inferior 1: "))
max1 = float(input("  Límite superior 1: "))

print("Defina el segundo intervalo (abierto):")
min2 = float(input("  Límite inferior 2: "))
max2 = float(input("  Límite superior 2: "))

print("Defina el tercer intervalo (abierto):")
min3 = float(input("  Límite inferior 3: "))
max3 = float(input("  Límite superior 3: "))

dentro_intervalo1 = x_intervalo > min1 and x_intervalo < max1
dentro_intervalo2 = x_intervalo > min2 and x_intervalo < max2
dentro_intervalo3 = x_intervalo > min3 and x_intervalo < max3

if dentro_intervalo1 or dentro_intervalo2 or dentro_intervalo3:
    print(f"\nEl número {x_intervalo} se encuentra DENTRO de al menos uno de los intervalos.")
else:
    print(f"\nEl número {x_intervalo} se encuentra FUERA de todos los intervalos.")