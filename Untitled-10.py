print("--- 1. Calculadora de Descuento (5%) ---")
costo = float(input("Ingrese el costo del artículo: $"))
valor_descuento = 0.0
if costo > 150000:
    print(f"El costo ${costo:,.0f} SÍ aplica para descuento.")
    valor_descuento = costo * 0.05
else:
    print(f"El costo ${costo:,.0f} NO aplica para descuento.")

print(f"El valor del descuento es: ${valor_descuento:,.2f}")