#17. Desarrollar un algoritmo que permita generar la colilla de pago 
# de los empleados de una empresa. La colilla debe mostrar:
# ●	El Salario del Empleado 
# ●	El Valor de Ahorro mensual programado.
# ●	La suma a deducir por aporte a la Salud (EPS) 12,5 %
# ●	La suma a deducir por aporte al Fondo de Pensiones  16%
# ●	Total a Recibir 
# ●	Toda la información que debe proveer el usuario del programa es el  Salario del Empleado y el Valor de Ahorro mensual programado.
#  El programa debe calcular y devolver el resto de los datos.4

while True:
    salario = float(input("Cual es tu salario?"))
    ahorro = float(input("Que porcentaje deseas ahorrar"))
    ahorrobb = ahorro/100
    print(f"deberias ahorrar {salario * ahorrobb} mensual")
    pago_salud = salario * 0.125
    print(f"Debes deducir en salud un {pago_salud}")
    pago_pension = salario * 0.16
    print(f"Tu pago de la pension debe debe de ser {pago_pension}")
    print(f"El total a recibir es: {salario - pago_salud - pago_pension - (salario * ahorrobb)}")
    salir = int(input("Si desea salir marque .1"))
    if salir == 1:
        break