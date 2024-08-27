class Conta:
    def __init__(self, numero, titular, saldo=0):
        """
        Construtor da classe Conta.
    
        Args:
            numero (int): O número da conta.
            titular (str): O nome do titular da conta.
            saldo (float, optional): O saldo inicial. Defaults to 0.
    
        Atributos:
            numero (int): O número da conta.
            titular (str): O nome do titular da conta.
            saldo (float): O saldo da conta.
            extrato (list): A lista de transações realizadas na conta.
        """
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def sacar(self, valor):
        """
        Efetua um saque na conta.
    
        Args:
            valor (float): Valor do saque.
    
        Retorna:
            Nada.
    
        Exceções:
            Nenhuma.
        """
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")

    def depositar(self, valor):
        """
        Efetua um depósito na conta.

        Args:
            valor (float): Valor do depósito.

        Retorna:
            Nada.

        Exceções:
            Nenhuma.
        """
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Valor inválido. O valor do depósito deve ser positivo.")

    def transferir(self, conta_destino, valor):
        """
        Efetua uma transferência entre duas contas.
        
        Args:
            conta_destino (Conta): A conta de destino da transferência.
            valor (float): Valor da transferência.
    
        Retorna:
            Nada.
    
        Exceções:
            Nenhuma.
        """
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.extrato.append(f"Transferência: R$ {valor:.2f} para {conta_destino.titular}")
            conta_destino.extrato.append(f"Recebido: R$ {valor:.2f} de {self.titular}")

    def consultar_extrato(self):
        """
        Exibe o extrato da conta, mostrando as transações efetuadas e o saldo atual.

        Nenhum argumento é necessário.

        Retorna:
            Nada.

        Exceções:
            Nenhuma.
        """
    
        print("\n================ EXTRATO ================")
        for transacao in self.extrato:
            print(transacao)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


# Criando contas
conta1 = Conta(123, "João", 1000)
conta2 = Conta(456, "Maria")

# Realizando operações
conta1.sacar(500)
conta1.depositar(200)
conta2.transferir(conta1, 300)

valor_deposito = float(input("Informe o valor do depósito: "))

conta2.depositar(valor_deposito)

valor_saque = float(input("Informe o valor do saque: "))

conta2.sacar(valor_saque)

# Consultando extrato
conta1.consultar_extrato()
conta2.consultar_extrato()