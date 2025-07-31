# Desafio Trilha Python DIO

## Desafio 1
#### Descrição
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

#### Depósito
* Deve ser possível depositar valores positivos para a minha conta bancária (v1 não precisa de identificação do usuário);
* Todos os depositos devem ser armazenados em uma variável para exibição no extrato

#### Saque
* Apenas 3 saques diários com o valor máximo de 500,00 por saque
* Se não houver saldo suficiente, deve ser exibida uma mensagem informando. 
* Todos os saques devem ser armazenados e exibidos no extrato

#### Extrato
* Deve listar todos os depósitos e saques
* Exibir no final o saldo atual da conta
* Os valores devem ser exibidos seguindo o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

## Desafio 2
#### Descrição
Deixar código mais modularizado criando funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 do sistema, deve-se criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com o usuário)

#### Cadastrar usuário (Cliente)
* O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, numero - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

#### Cadastrar conta bancária
* O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

