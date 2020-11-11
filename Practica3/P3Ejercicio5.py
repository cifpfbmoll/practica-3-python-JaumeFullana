#Pida un número que como máximo tenga tres cifras (por ejemplo serían válidos 1,
#99 i 213 pero no 1001). Si el usuario introduce un número de más de tres cifras 
#debe un informar con un mensaje de error como este “ERROR: El número 1005 tiene 
#más de tres cifras”.
numero=input("Buenas! introduzca un numero de 3 cifras como maximo")
if (int(numero)<1000):
    print ("Gracias!")
else:
    print ("ERROR: El número", numero, "tiene más de tres cifras")