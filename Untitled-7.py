nota = float(input("ingrese su nota definitiva"))
if nota < 3.0:
    print ("Insuficiente")
else:
    if nota <= 3.5:
        print ("Aceptable")
    else:
        if nota <= 4.0:
            print ("Sobresaliente")
        else:
            if nota <= 5.0:
                print ("Excelente")