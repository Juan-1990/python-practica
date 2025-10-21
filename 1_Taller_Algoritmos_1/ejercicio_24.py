#24.Un estudiante realiza un préstamo a un plazo de 5 años, donde la tasa fija de interés es del 5% anual, se debe solicitar el monto del préstamo y se desea calcular la siguiente información. 
# • Cuanto dinero se ha pagado de intereses en un año. 
# • Cuanto dinero se ha pagado de intereses en el tercer trimestre del año. 
# • Cuanto dinero se ha pagado de intereses en el primer mes. 
# • Cuanto dinero se paga en total del préstamo solicitado incluyendo intereses. 
# Solicitar el monto del préstamo
monto = float(input("Ingrese el monto del préstamo: "))

# Datos del préstamo
tasa_anual = 0.05 
plazo_anios = 5

# Cálculos
interes_anual = monto * tasa_anual
interes_trimestre = interes_anual / 4   # un año tiene 4 trimestres
interes_mes = interes_anual / 12        # un año tiene 12 meses
interes_total = interes_anual * plazo_anios
total_pagar = monto + interes_total

# Resultados
print(f"\n--- RESULTADOS ---")
print(f"Interés pagado en un año: ${interes_anual:,.2f}")
print(f"Interés pagado en el tercer trimestre del año: ${interes_trimestre:,.2f}")
print(f"Interés pagado en el primer mes: ${interes_mes:,.2f}")
print(f"Total a pagar (monto + intereses): ${total_pagar:,.2f}")