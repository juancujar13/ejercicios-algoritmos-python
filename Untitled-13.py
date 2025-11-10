print("--- Ejercicio 4: Calcular promedio del curso ---")

nota1 = float(input("Ingrese la nota del trabajo 1 (0.0 - 5.0): "))
nota2 = float(input("Ingrese la nota del trabajo 2 (0.0 - 5.0): "))
nota3 = float(input("Ingrese la nota del trabajo 3 (0.0 - 5.0): "))
nota4 = float(input("Ingrese la nota del trabajo 4 (0.0 - 5.0): "))
nota5 = float(input("Ingrese la nota del trabajo 5 (0.0 - 5.0): "))
nota_definitiva = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
if nota_definitiva >= 3.5:
    print(f"El estudiante GANÓ el curso.")
else:
    print(f"El estudiante PERDIÓ el curso.")
print(f"La nota final es:", nota_definitiva)