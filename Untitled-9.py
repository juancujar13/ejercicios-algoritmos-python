print("--- Calculadora de Descuentos (Ejemplo 3.13) ---")
precio_articulo = float(input("Ingrese el precio del artículo: "))
tipo_articulo = int(input("Ingrese el tipo de artículo (1, 2, 3 u Otro): "))

porcentaje_descuento = 0.0
    
if tipo_articulo == 1:
        porcentaje_descuento = 0.125
else:
    if tipo_articulo == 2:
        porcentaje_descuento = 0.083
    else:
        if tipo_articulo == 3:
            porcentaje_descuento = 0.032
        else:
            porcentaje_descuento = 0.0

    valor_descuento = precio_articulo * porcentaje_descuento
    print ("El valor de descuento es",valor_descuento)