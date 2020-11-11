#Pida al usuario el espacio recorrido por un coche y el tiempo que ha tardado en 
#horas y que calcule a qué velocidad media había realizado el recorrido.
print ("Buenas, aqui puede calcular la velocidad media a la que ha hecho su \
viaje")
distancia=input("Cuantos km ha recorrido el coche?")
tiempo=input("Cuantos minutos ha tardado en recorrer esos km?")
tiempoHoras=int(tiempo)/60
velocidad=float(distancia)/float(tiempoHoras)
print ("La velocidad media a la que ha viajado su coche es:", int(velocidad),\
"km/h")