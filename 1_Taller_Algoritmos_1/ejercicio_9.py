# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuánto dinero obtendrá por 
# concepto de comisiones por las tres ventas que realiza 
# en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
sueldo_base = float(input("Ingresa el sueldo base"))
comisiones = sueldo_base * 0.10
print(f"El total del sueldo es {sueldo_base} y las comisiones son {comisiones}, para un total de: {sueldo_base + comisiones}")