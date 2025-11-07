nota = float(input("Ingresa la nota definitiva (0.0 a 5.0): "))
print(f"La nota ingresada es: {nota}")
if 0.0 <= nota <= 5.0:
    if nota >= 4.0:
        print("¡Felicitaciones, excelente desempeño!")
else:
    print("La nota ingresada está fuera del rango permitido.")
