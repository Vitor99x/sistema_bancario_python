from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco, contas=None):
        self.endereco = endereco
        self.contas = contas if contas is not None else []

    def realizar_transacao(self, conta, transacao):
        sucesso = transacao.registrar(conta)
        if sucesso:
            print("Transação realizada com sucesso.")
        else:
            print("Falha na transação.")

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco, contas=None):
        super().__init__(endereco, contas)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def exibir_saldo(self):
        print(f"Saldo: R${self.saldo:.2f}")

    @staticmethod
    def nova_conta(cliente, numero, agencia):
        return Conta(saldo=0.0, numero=numero, agencia=agencia, cliente=cliente, historico=Historico())
    
    def sacar(self, valor):
        if self.saldo < valor:
            print("Falha no saque: saldo insuficiente.")
            return False
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} efetuado.")
            return True
            
    def depositar(self, valor):
        if valor <= 0:
            print("Falha no depósito: valor inválido.")
            return False
        else:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} efetuado.")
            return True

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass
    
class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: Conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar(f"Depósito: R${self.valor:.2f}")
        return sucesso

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: Conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar(f"Saque: R${self.valor:.2f}")
        return sucesso

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, descricao):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.transacoes.append(f"[{data}] {descricao}")

    def exibir(self):
        for transacao in self.transacoes:
            print(transacao)

# --- Teste ---
cliente = PessoaFisica("Vitor", "206.062.088-00", "1999-12-25", "Rua da Consolação, 382")
conta = Conta(saldo=100.0, numero="0001", agencia="001", cliente=cliente, historico=Historico())
print(f"saldo inicial: {conta.saldo}")

cliente.adicionar_conta(conta)

deposito = Deposito(50.0)
cliente.realizar_transacao(conta, deposito)
conta.exibir_saldo()

saque = Saque(30.0)
cliente.realizar_transacao(conta, saque)

conta.exibir_saldo()
conta.historico.exibir()
