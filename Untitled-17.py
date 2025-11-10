print("\n--- Ejercicio 8: Calcular descuento por tipo de artículo ---")

print("Seleccione el tipo de artículo:")
print("1. Textil")
print("2. Electrodoméstico")
print("3. Elementos de cocina")
print("4. Video juego")

opcion_tipo = input("Ingrese el número (1-4): ")
precio_articulo = float(input("Ingrese el precio del artículo: $"))

porcentaje_descuento = 0.0
tipo_texto = "Desconocido"

if opcion_tipo == "1":
    porcentaje_descuento = 0.0
    tipo_texto = "Textil"
elif opcion_tipo == "2":
    porcentaje_descuento = 3.7
    tipo_texto = "Electrodoméstico"
elif opcion_tipo == "3":
    porcentaje_descuento = 4.2
    tipo_texto = "Elementos de cocina"
elif opcion_tipo == "4":
    porcentaje_descuento = 7.8
    tipo_texto = "Video juego"
else:
    print("Opción no válida, no se aplicará descuento.")

valor_descuento = precio_articulo * (porcentaje_descuento / 100)
precio_final = precio_articulo - valor_descuento

print(f"\n--- Resumen ---")
print(f"Artículo: {tipo_texto}")
print(f"Precio original: ${precio_articulo:.2f}")
print(f"Descuento ({porcentaje_descuento}%): ${valor_descuento:.2f}")
print(f"Precio final a pagar: ${precio_final:.2f}")