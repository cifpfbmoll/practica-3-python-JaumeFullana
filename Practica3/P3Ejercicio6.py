#Pida al usuario el precio de un producto y el nombre del producto y muestre el 
#mensaje con el precio del IVA (21%). Por ejemplo: “Tu bicicleta vale 100 euros
#y con el 21 % de IVA se queda en 121 euros en total”.
precio=input("Buenas! cuanto cuesta el producto que desea comprar?")
nombre=input("Podria indicarme el nombre del producto?")
IVA=(float(precio)*21)/100
total=float(precio)+float(IVA)
print ("Tu", nombre,"vale", precio,"euros y con el 21 % de IVA se queda en"\
, total,"euros en total")