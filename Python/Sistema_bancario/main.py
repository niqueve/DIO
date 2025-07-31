from Banco import Caixa_eletronico
from Sistema import Sistema

#-------------------------------------função principal
sistema = Sistema()
banco = Caixa_eletronico(1500)

def main ():
    while True:
        opcao = sistema.menu()
        match opcao:
            case 1:
                operacao = sistema.cadastrar_usuario()
                print(operacao)
            case 2:
                operacao = sistema.cadastrar_conta()
                print(operacao)
            case 3:
                sistema.caixa_eletronico()

            case 4:
                print("Encerrando..")
                break

if __name__ == "__main__":
    main()