# En una universidad los estudiantes pueden pagar 
# el valor de su matrícula en cuatro cuotas de la siguiente forma 
#●  Primera cuota: 40% 
#●  Segunda cuota: 25%
#●  Tercera cuota: 20% 
#●  Cuarta cuota: 15% 
# Diga cuanto es el valor que tiene que pagar por cuota un estudiante.

valor_matricula = float(input("Ingrese el valor total de la matrícula: "))


primera_cuota = valor_matricula * 0.40
segunda_cuota = valor_matricula * 0.25
tercera_cuota = valor_matricula * 0.20
cuarta_cuota = valor_matricula * 0.15

print(f"Primera cuota 40%: {primera_cuota:,.2f}")
print(f"Segunda cuota 25%: {segunda_cuota:,.2f}")
print(f"Tercera cuota 20%: {tercera_cuota:,.2f}")
print(f"Cuarta cuota 15%: {cuarta_cuota:,.2f}")
print(f"Total a pagar: ${primera_cuota + segunda_cuota + tercera_cuota + cuarta_cuota: .2f}")