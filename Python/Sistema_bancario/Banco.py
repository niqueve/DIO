
class Caixa_eletronico:

    def __init__(self, saldo):
        self.saldo = saldo
        self.movimentacoes = []
        self.LIMITE_SAQUE = 3
        self.MAX_SAQUE = 500
        self.controle_operacao = 0
    
    def __str__(self):
        return f"Saldo em conta {self.saldo} \n Limite de saque {self.LIMITE_SAQUE} \n valor máximo por saque {self.MAX_SAQUE}"

    def saque (self):
        valor_saque = float(input("Digite o valor para saque: "))
        if self.controle_operacao < self.LIMITE_SAQUE:
            if valor_saque > self.saldo:
                return f"Operação recusada. \n Saldo menor que valor selecionado para saque"
            elif valor_saque > self.MAX_SAQUE:
                return f"Operação recusada. \n {valor_saque} excede limite por saque de 500"
            else:
                saldo_anterior = self.saldo
                self.saldo = saldo_anterior - valor_saque
                texto_extrato = f"Operacao de saque - saldo anterior R${saldo_anterior:.2f} - retirada R${valor_saque:.2f} - saldo em conta R${self.saldo:.2f}"
                self.movimentacoes.append(texto_extrato)
                self.controle_operacao += 1
                return texto_extrato
        else:
            return f"Operação recusada \n O limite de {self.LIMITE_SAQUE} saques diários foi atingido"
    
    def deposito (self):
        valor_deposito = float(input("Digite o valor do deposito: "))
        if valor_deposito > 0:
            saldo_anterior = self.saldo
            self.saldo = saldo_anterior + valor_deposito
            texto_extrato = f"Operacao de Depósito - saldo anterior R${saldo_anterior:.2f} - Depósito de R${valor_deposito:.2f} - saldo em conta R${self.saldo:.2f}"
            self.movimentacoes.append(texto_extrato)
            return texto_extrato
        else:
            print("valor inválido. Só serem permitidos depósitos com valores maiores que 0")

    def extrato (self):
        print('\n #### EXTRATO ##### \n' )
        for operacao in self.movimentacoes:
            print(operacao)
        print(f"\n Saldo atual da conta: {self.saldo} \n")
        