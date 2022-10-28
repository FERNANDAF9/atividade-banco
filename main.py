# MENUS
menu_extrato = \
    ('''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
                     EXTRATO
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
            ''')
menu_deposito = \
    ('''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
                   DEPÓSITOS
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
            ''')
menu_saque = \
    ('''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
                     SAQUE
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
                    ''')
menu_principal = \
    (''' 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                BANCO LISTRAS

As operações disponíveis estão listadas abaixo:

    (1) - Depósito
    (2) - Saque
    (3) - PIX
    (4) - Extrato Bancário
    (5) - Sair

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
    ''')

menu_pix = \
    ('''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
                      PIX
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    

    (1) - CPF
    (2) - Celular
    (3) - Chave aleatória
    (4) - Email

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   

''')


def verifica_saldo_pix(valor_do_pix):
    global saldo, lista_pix
    valor_do_pix = float(valor_do_pix)
    if (valor_do_pix > saldo):
        print(f'Saldo insuficiente para realizar o PIX. Seu saldo atual é R${saldo:.2f}.')
        resposta = input('Deseja tentar novamente?s/n: ')
        checa_resposta(resposta)
        if (resposta == 's'):
            novo_pix()
        else:
            resposta_nao()
    else:
        lista_pix.append(valor_do_pix)
        print('Pix realizado com sucesso')
        saldo -= valor_do_pix
        resposta = input('Deseja realizar outro PIX?s/n: ')
        resposta = checa_resposta(resposta)
        if (resposta == 's'):
            novo_pix()
        else:
            resposta_nao()


# CALCULO DO SALDO ATUAL

saldo_inicial = 1000.0
lista_depositos = []
lista_saques = []
lista_pix = []
limite_saques_diarios = 3
teste = saldo_inicial - sum(lista_saques) + sum(lista_depositos) - sum(lista_pix)
saldo = teste


# RESPONDEU NÃO
def resposta_nao():
    resposta = int(input('\nDigite (1) para voltar ao menu principal ou (0) para sair: '))
    while (resposta != 0 and resposta != 1):
        resposta = int(input('Por favor, digite uma opção válida: '))

    if (resposta == 1):
        return main()
    else:
        print('Obrigada por utilizar nossos serviços!')
        exit()


# CHECA A OPÇÃO SELECIONADA NO MENU.
def checa_opcao_menu(opcao):
    é_numero = opcao.isdigit()
    while (é_numero == False):
        opcao = input('Digite apenas números: ')
        é_numero = opcao.isdigit()

    opcao = int(opcao)
    while (opcao < 1 or opcao > 5):
        opcao = int(input('Digite uma opção válida: '))
    return opcao


# ----------------------------------------------------------------------------------------
# CHECA A OPÇÃO SELECIONADA NO PIX
def checa_opcao_pix(opcao):
    opcao = int(opcao)
    while (opcao < 1 and opcao > 4):
        opcao = int(input('Digite uma opção válida: '))
    return opcao


# ----------------------------------------------------------------------------------------
# FUNÇÃO QUE CHECA SE O VALOR É VALIDO....
def validação_do_valor(valor):
    valor = float(valor)
    while (valor <= 0):
        valor = float(input('Valor inválido, por favor, digite um valor válido: '))
    return valor


# FUNÇÃO QUE CHECA A PERGUNTA S/N
def checa_resposta(resposta):
    resposta = resposta.lower()
    while (resposta != 'n' and resposta != 's'):
        resposta = input('Digite uma opçao válida: ')
    return resposta


# CHECA CPF
def checa_cpf(cpf):
    é_cpf = cpf.isdigit()
    while (len(cpf) != 11 or é_cpf == False):
        cpf = input('Digite um CPF válido')
        é_cpf = cpf.isdigit()

    valor = input('Digite o valor do PIX: ')
    valor = validação_do_valor(valor)
    verifica_saldo_pix(valor)


# CHECA CELULAR
def checa_celular(celular):
    é_celular = celular.isdigit()
    while (len(celular) != 10 or é_celular == False):
        celular = input('Digite um celular válido!: ')
        é_celular = celular.isdigit()

    valor = input('Digite o valor do PIX: ')
    valor = validação_do_valor(valor)
    verifica_saldo_pix(valor)


# CHECA EMAIL
def checa_email(email):
    while (email.count('@') != 1) or (email.count('.com') != 1):
        email = input('Digite um email válido: ')

    valor = input('Digite o valor do PIX: ')
    valor = validação_do_valor(valor)
    verifica_saldo_pix(valor)


# CHECA CAHVE ALEATÓRIA
def checa_chave_aleatoria(chave):
    while (len(chave) != 32):
        chave = input('Digite uma chave válida!: ')

    valor = input('Digite o valor do PIX: ')
    valor = validação_do_valor(valor)
    verifica_saldo_pix(valor)


# FUNÇÃO NOVO DEPÓSITO
def novo_deposito(resposta):
    global lista_depositos, saldo
    print(resposta)
    if (resposta == 's'):
        deposito = float(input('Digite o valor do depósito: '))
        validação_do_valor(deposito)
        lista_depositos.append(deposito)
        saldo += deposito
        resposta = input('Depósito realizado com sucesso!\nDeseja realizar novo depósito? s/n ')
        resposta = checa_resposta(resposta)
        novo_deposito(resposta)

    else:
        resposta_nao()


# NOVO PIX
def novo_pix():
    print(menu_pix)
    tipo_chave = int(input('Informe a opção desejada: '))
    tipo_chave = checa_opcao_pix(tipo_chave)
    resposta = tipo_de_pix(tipo_chave)
    if (resposta == 's'):
        novo_pix()
    else:
        resposta = int(input('Digite (1) para voltar ao menu principal ou (0) para sair: '))
        while (resposta != 0 and resposta != 1):
            resposta = input('Por favor, digite uma opção válida: ')

        if (resposta == 1):
            return main()
        else:
            print('Obrigada por utilizar nossos serviços!')
            exit()


# MENU DO PIX
def tipo_de_pix(tipo_chave):
    if (tipo_chave == 1):
        cpf = input('Digite o CPF: ')
        checa_cpf(cpf)
        resposta = input('Deseja realizar um novo PIX? s/n ')
        resposta = checa_resposta(resposta)
        return resposta
    elif (tipo_chave == 2):
        celular = input('Digite o celular: ')
        checa_celular(celular)
        resposta = input('Deseja realizar um novo PIX? s/n ')
        resposta = checa_resposta(resposta)
        return resposta
    elif (tipo_chave == 3):
        chave_aleatória = input('Digite a chave aleatória: ')
        checa_chave_aleatoria(chave_aleatória)
        resposta = input('Deseja realizar um novo PIX? s/n ')
        resposta = checa_resposta(resposta)
        return resposta
    elif (tipo_chave == 4):
        email = input('Digite o email: ')
        checa_email(email)
        resposta = input('Deseja realizar um novo PIX? s/n ')
        resposta = checa_resposta(resposta)
        return resposta


####################################  CODIGO PRINCIPAL  #######################################

def novo_saque():
    global saldo, limite_saques_diarios, lista_saques, lista_depositos
    valor_saque = input('Digite o valor do saque: ')
    valor_saque = validação_do_valor(valor_saque)

    # Se der erro
    while (valor_saque > saldo or valor_saque > 500 or limite_saques_diarios == 0):
        if (valor_saque > saldo):
            print(f'Saldo insuficiente, seu saldo atual é R${saldo:.2f}')
            resposta = input('Deseja continuar? s/n: ')
            resposta = checa_resposta(resposta)
            if (resposta == 's'):
                novo_saque()
            else:
                resposta_nao()

        elif (valor_saque > 500):
            print('O valor máximo por saque é de R$500,00')
            resposta = input('Deseja tentar novamente? s/n: ')
            resposta = checa_resposta(resposta)
            if (resposta == 's'):
                novo_saque()
            else:
                resposta_nao()
        else:
            print('Você atingiu o limite de saques diários!\nO número máximo de saques diários é 3!')
            resposta_nao()

    lista_saques.append(valor_saque)
    limite_saques_diarios -= 1
    print('Saque realizado com sucesso!')
    saldo -= valor_saque
    resposta = input('Deseja realizar um novo saque?s/n: ')
    resposta = checa_resposta(resposta)
    if (resposta == 's'):
        novo_saque()
    else:
        resposta_nao()


def main():
    global lista_depositos, saldo, lista_saques
    print(menu_principal)
    opcao_cliente = input('Informe a opção desejada: ')
    opcao_cliente = checa_opcao_menu(opcao_cliente)

    if (opcao_cliente == 1):  # deposito
        global saldo
        print(menu_deposito)
        valor_deposito = input('Digite o valor do depósito: ')
        valor_deposito = validação_do_valor(valor_deposito)
        lista_depositos.append(valor_deposito)
        saldo += valor_deposito
        resposta = input('Depósito realizado com sucesso!\nDeseja realizar novo depósito? s/n ')
        checa_resposta(resposta)
        novo_deposito(resposta)

    elif (opcao_cliente == 2):  # saque
        print(menu_saque)
        novo_saque()

    elif (opcao_cliente == 3):  # pix
        novo_pix()

    elif (opcao_cliente == 4):  # extrato
        print(menu_extrato)
        for i in range(len(lista_depositos)):
            # >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >> >>
            print(f'DEPÓSITO                                 +R${lista_depositos[i]:.2f}')
        for i in range(len(lista_saques)):
            print(f'SAQUE                                    -R${lista_saques[i]:.2f}')
        print('--------------------------------------------------\n')
        print(f'SALDO                                     R${saldo:.2f}')


# CHAMA A FUNÇÃO MAIN
if __name__ == "__main__":
    main()
