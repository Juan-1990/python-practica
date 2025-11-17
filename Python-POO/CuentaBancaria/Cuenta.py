class Cuenta:
    def __init__(self, NumeroCuenta, titular, saldo, fecha):
        self._NumeroCuenta = NumeroCuenta
        self._titular = titular
        self._saldo = saldo
        self._fecha = fecha

    def set_NumeroCuenta(self, NumeroCuenta):
        self._NumeroCuenta = NumeroCuenta

    def set_titular(self, titular):
        self._titular = titular

    def set_saldo(self, saldo):
        self.saldo = saldo
    
    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_estado(self, estado):
        self._estado = estado

    def get_NumeroCuenta(self):
        return self._NumeroCuenta

    def get_titular(self):
        return self._titular
    
    def get_saldo(self):
        return self._saldo
    
    def get_fecha(self):
        return self._fecha
    
    def get_estado(self):
        return self._estado
    
    def DepositarDinero(self, monto):
        if monto <= 0:
            print("El monto a depositar debe serr mayor que 0")
            return
        else: 
            self._saldo += monto
            print(f"Deposito de {monto} realizado. Saldo actual: {self._saldo}")

    def RetirarDinero(self, monto):
        if monto > self._saldo:
            print(f"Fondos insuficientes. Saldo actual {self._saldo}")
        else:
            self._saldo -= monto
            print(f"Retiro realizado. Saldo actual: {self._saldo}")

    def ConsultarSaldo(self):
       print(f"Cuenta N° {self._NumeroCuenta}")
       print(f"Titular: {self._titular}")
       print(f"Saldo: {self._saldo}")
       print(f"Fecha de apertura: {self._fecha}")
