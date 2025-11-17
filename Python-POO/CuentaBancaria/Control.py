from Cuenta import Cuenta

Usuario1 = Cuenta(3002679765, "Camilo Vargas", 4000000, "2025-11-13")

print(f"El titular de la cuenta es {Usuario1.get_titular()}\n el numero de la cuenta es {Usuario1.get_NumeroCuenta()}")

Usuario1.DepositarDinero(700000)
Usuario1.RetirarDinero(200000)

Usuario1.ConsultarSaldo()
