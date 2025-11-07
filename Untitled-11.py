print("\n--- 2. Control del Tanque de Agua (Rango: 250-450L) ---")
litros_actuales = float(input("Ingrese los litros actuales del tanque: "))
if litros_actuales < 250:
    print(f"Nivel actual: {litros_actuales}L. (Nivel bajo)")
    print("Acción: ABRIR la llave.")
        
elif litros_actuales > 450:
        print(f"Nivel actual: {litros_actuales}L. (Nivel alto)")
        print("Acción: CERRAR la llave.")
else:
    print(f"Nivel actual: {litros_actuales}L. (Nivel óptimo)")
    print("Acción: MANTENER estado actual.")