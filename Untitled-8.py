num1 = float(input("Ingrese el primer numero"))
num2 = float(input("Ingrese el segundo numero"))
num3 = float(input("Ingrese el tercer numero"))
num4 = float(input("Ingrese el cuarto numero"))
if num1 > num2 and num1 > num3 and num1 > num4:
    print ("El numero mayor es", num1)
else:
    if num2 > num1 and num2 > num3 and num2> num3:
        print("El numero mayor es", num2)
    else:
        if num3 > num1 and num3 > num2 and num3 > num4:
            print("el numero mayor es", num3)
        else:
            if num4 >num1 and num4 >num2 and num4 > num3:
                print ("El numero mayor es", num4)