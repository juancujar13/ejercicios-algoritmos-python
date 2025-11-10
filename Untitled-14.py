print("\n--- Ejercicio 5: Verificar solución de ecuación cuadrática ---")

a = float(input("Ingrese el valor del coeficiente a: "))
b = float(input("Ingrese el valor del coeficiente b: "))
c = float(input("Ingrese el valor del coeficiente c: "))
discriminante = (b**2) - (4 * a * c)
if discriminante >= 0 and a != 0:
    print("La ecuación cuadrática tiene solución.")
else:
    print("La ecuación cuadrática no tiene solución.")