menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> '''

saldo = 0
extrato = ""
limite = 500
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        # DEPOSITO
        valor = float(input("Qual valor deseja depositar? "))

        if valor > 0:
            saldo += valor
            print(f"Você depositou R${valor:.2f}\n")
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operaçaõ falhou. O valor informado é invalido!")

    elif opcao == "s":
        # SAQUE
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numeros_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação Falhou! Valor de saque excede o limite!")

        elif excedeu_saques:
            print("Operação Falhou! Você ja atingiu o limite de saques!")

        elif valor > 0:
            saldo -= valor
            print(f"Você fez um saque de R${valor:.2f}\n")
            extrato += f"Saque: R${valor:.2f}\n"
            numeros_saques += 1

        else:
            print("Operação Falhou! O valor informado é invalido!")

    elif opcao == "e":
        # EXTRATO
        print("\n===============EXTRATO==============")
        print("Não foram realizadas movimentações na sua conta bancaria." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")

    elif opcao == "q":
        # EXIT
        print("Saindo")
        break
    else:
        print("Operacao invalida, por favor selecione a opcao desejada!")
