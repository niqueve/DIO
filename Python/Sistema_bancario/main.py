from Banco import Caixa_eletronico

#------------------------------menu
def menu ():
    resposta = int(input("Digite o número da operação desejada: \n" \
    "1 - Saque \n" \
    "2 - Depósito \n" \
    "3 - Extrato \n" \
    "4 - Sair \n"))
    return resposta

#-------------------------------------função principal
banco = Caixa_eletronico(1500)

def main ():
    while True:
        opcao = menu()
        match opcao:
            case 1:
                operacao = banco.saque()
                print(operacao)
            case 2:
                operacao = banco.deposito()
                print(operacao)
            case 3:
                banco.extrato()

            case 4:
                print("Encerrando..")
                break

if __name__ == "__main__":
    main()