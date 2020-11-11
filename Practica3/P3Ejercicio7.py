#Pida al usuario tres número que serán el día, mes y año. Comprueba que la fecha
#introducida es válida.  Por ejemplo: 
#32/01/2017->Fecha incorrecta
#29/02/2017->Fecha incorrecta
#30/09/2017->Fecha correcta.

dia=int(input("Buenas! podria indicarme el dia?"))
mes=int(input("Gracias! ahora necesitaria saber el mes:"))
ano=int(input("Muchas Gracias! para terminar seria tan amable de indicarme el año:"))

if(1>mes or mes>12):
    print ("ERROR: El",dia,"/",mes,"/",ano,"es incorrecto.")
elif (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and (1>dia or dia>31):
    print ("ERROR: El",dia,"/",mes,"/",ano,"es incorrecto.")
elif (mes==4 or mes==6 or mes==9 or mes==11) and (1>dia or dia>30):
    print ("ERROR: El",dia,"/",mes,"/",ano,"es incorrecto.")
elif (mes==2):
    if (ano%4==0) and (1>dia or dia>29):
        print ("ERROR: El",dia,"/",mes,"/",ano,"es incorrecto.")
    elif (ano%4!=0) and (1>dia or dia>28):
        print ("ERROR: El",dia,"/",mes,"/",ano,"es incorrecto.")
    else:
          print ("El",dia,"/",mes,"/",ano,"es correcto.")
    
else:
    print ("El",dia,"/",mes,"/",ano,"es correcto.")


