from Banco import Conta_corrente, Usuario

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.contas = {}

    #------------------------------menu
    def menu (self):
        resposta = int(input("Digite o número da operação desejada: \n" \
        "1 - Cadastrar usuário \n" \
        "2 - Criar Conta \n" \
        "3 - Operações \n" \
        "4 - Sair \n"))
        return resposta
    

    #---------------------------------------------cadastro de usuário
    def cadastrar_usuario(self):
        cpf = input("digite o número do cpf sem pontos e traços ex: 12358265855: ")
        verifica = self.verificar_usuario(cpf)
        if  verifica == True:
            print("usuário já cadastrado")
        else:
            nome = input("Digite seu nome")
            nascimento = input('Digite a data de nascimento:')
            endereco = input("Digite o endereço seguindo o formato: logradouro, numero - bairro - cidade/sigla estado \n")
            usuario = Usuario(nome, nascimento, cpf, endereco)
            self.usuarios.append(usuario) 
            print("usuário cadastrado")
    
    #--------------------------------------------------verificar se cpf informado pertence a um usuário ja existente
    def verificar_usuario (self, num_cpf):
        for usuario in self.usuarios:
            if num_cpf == usuario.cpf:
                return True
            else:
                return False     
    #-------------------------------------------------cadastro de conta
    def cadastrar_conta (self):
        num_conta = len(self.contas) + 1
        usuario = input("digite o número do cpf sem pontos e traços ex: 12358265855: ")
        conta = Conta_corrente(num_conta, usuario)
        usuarios_existentes = self.contas.keys()
        if usuario in usuarios_existentes:
            contas_listadas = self.contas[usuario]
            contas_listadas.append(conta)
            self.contas[usuario] = contas_listadas
        else:
            self.contas[usuario] = [conta]

        print("conta cadastrada")

    #-------------------------------------------------operações
    def caixa_eletronico (self, caixa):
        while True:
            #print("* pressione qualquer outra tecla caso queira retornar ao menu anterior")
            opcao = caixa.menu()
            match opcao:
                case 1:
                    operacao = caixa.saque()
                    print(operacao)
                case 2:
                    operacao = caixa.deposito()
                    print(operacao)
                case 3:
                    caixa.extrato()
                case 4:
                    print("Encerrando..")
                    break
            
