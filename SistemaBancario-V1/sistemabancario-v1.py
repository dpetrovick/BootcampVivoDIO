from time import sleep
# cabeçalho
print('\n')
print(f'\033[30;44m {"-=" * 35}\033[m')  # Primeira linha cheia
print(f'\033[30;44m -= \033[m', '\033[30;44m =- \033[m'.rjust(77))  # Segunda linha inicio e fim (borda)
print(f'\033[30;44m -= \033[m', '\033[1;30;44m Banco Internacional DIO \033[m'.center(74),
      f'\033[30;44m =- \033[m'.rjust(15))  # Nome e borda
print(f'\033[30;44m -= \033[m', '\033[30;44m =- \033[m'.rjust(77))  # linha abaixo do nome (borda)
print(f'\033[30;44m {"-=" * 35}\033[m')  # ultima linha cheia.
print('\n')

# Código
saldo = conta_saque = 0
atualiza_movimentacao = {}
movimentacao_deposito = []
movimentacao_saque = []
while True:
    print(f'''
    \033[30;44m{"-=" * 20}\033[m\n
           \033[34m 1 - Depósito\033[m
           \033[34m 2 - Saque\033[m
           \033[34m 3 - Extrato\033[m
           \033[34m 4 - sair\033[m\n
    \033[30;44m{"-=" * 20}\033[m
            ''')
    menu = int(input('     Informe sua opção: '))  # escolha das opções do Menu
    if menu == 1:# Opção de depósito - Soma o valor depositado ao saldo.
        print()
        valor_deposito = float(input('     Informe o valor a ser depositado em sua conta: R$ ')) # Valor depositado
        movimentacao_deposito.append(valor_deposito) # Inseri o valor na lista de depósito
        atualiza_movimentacao['Depósito'] = movimentacao_deposito # Recebe a lista no dic. depósito.
        saldo += valor_deposito
        print(f'\033[1:33m      Valor R${valor_deposito:.2f} depositado com sucesso!\033[m')
        sleep(2)

    elif menu == 2:  # Opção saque - Verifica se é o 3º saque, se tem saldo e o valor do saque ultrapassa o saldo
        print()
        if conta_saque == 3:  # Verifica se é o 3 saque
            print('\033[1:33m     Limite diário de 3 saques atingido!\033[m')
            sleep(2)
        elif saldo == 0:  # verifica se tem saldo disponível
            print('\033[1:33m     Saque indisponível! Seu saldo é R$ 0,00. Faça um depósito primeiro\033[m')
            sleep(2)
        elif saldo > 0:  # Tendo saldo para saque...
            valor_saque = float(input('     Informe o valor que deseja sacar: R$ '))
            if valor_saque > saldo:  # Verifica se o saque é maior que o saldo disponível
                print('\033[1:31m     Saldo insuficiente!\033[m')
                print(f'     Seu saldo atual é: R$ {saldo}')
                while valor_saque > saldo:
                    valor_saque = float(input(f'     Informe o valor que deseja sacar até R$ {saldo}: R$ '))
                    if valor_saque <= saldo:  # se o valor de saque for menor que o saldo, realiza o saque
                        movimentacao_saque.append(valor_saque)
                        atualiza_movimentacao['Saque'] = movimentacao_saque
                        saldo -= valor_saque
                        conta_saque += 1
                        print(f'\033[1:33m     Saque de R$ {valor_saque} realizado com Sucesso!\033[m')
                        sleep(2)
                        continue
            elif valor_saque > 500:  # Verifica se o valor do saque é maior que R$ 500,00
                print(f'\033[1:33m    Valor R$ {valor_saque} do saque é maior que o limite máximo de saque de R$ 500,00\033[m')
                while valor_saque > 500:
                    valor_saque = float(input('     Informe o valor que deseja sacar até R$ 500,00: R$ '))
                    if valor_saque <= 500:
                        movimentacao_saque.append(valor_saque)
                        atualiza_movimentacao['Saque'] = movimentacao_saque
                        saldo -= valor_saque
                        conta_saque += 1
                        print(f'\033[1:33m     Saque de R$ {valor_saque} realizado com Sucesso!\033[m')
                        sleep(2)
            else:
                movimentacao_saque.append(valor_saque)
                atualiza_movimentacao['Saque'] = movimentacao_saque
                saldo -= valor_saque
                conta_saque += 1
                print(f'\033[1:33m     Saque de R$ {valor_saque} realizado com Sucesso!\033[m')
                sleep(2)

    elif menu == 3:  # Opção extrato -  Mostra a movimentação da conta
        print(f'\n{"## EXTRATO ##":^35}\n')
        if 'Depósito' in atualiza_movimentacao:
            print('\033[1:34m     Depósitos:\033[m')
            for valor in atualiza_movimentacao['Depósito']:
                print(f'\033[1:32m    + R$ {valor}\033[m')
        else:
            print(f'''\033[1:34m     Depósitos:\033[m
        R$ 0,00''')
        print()
        if 'Saque' in atualiza_movimentacao:
            print('\033[1:34m     Saques:\033[m')
            for valor in atualiza_movimentacao['Saque']:
                print(f'\033[1:31m    - R$ {valor}\033[m')
        else:
            print(f'''\033[1:34m     Saque:\033[m
        R$ 0,00''')
        print(f'\n\033[1:32m    Seu saldo é R$ {saldo:.2f}.\033[m')
        sleep(2)

    elif menu == 4:
        print()
        print('\033[1:31m     Você escolheu sair do programa\033[m')
        sleep(1.4)
        print('     Encerrando o programa', end='')
        for i in range (0, 6):  # Funcionou no Pycharm mas não no vscode
              print('.', end='')
              sleep(.5)
        break
    else:
        print('\033[31m   Opção errada!! Tente novamente!\033[m')
print('\n')
print('\033[1:33mPrograma encerrado com sucesso! Volte sempre!!\033[m')