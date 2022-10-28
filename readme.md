## :file_folder: Programa em python de gerenciamento de valores de um banco

## :beginner: Objetivos:
O objetivo desse programa é estudar acerca de funções, variaveis globais, validações de strings e números, operadores e estruturas condicionais.

## O programa:
O programa possui inicialmente um menu, com escolhas enumeradas de 1 a 5.

<div align=center>
  <img  width=400 src= 'https://user-images.githubusercontent.com/56310579/198419444-56ba73c0-b015-421a-917a-12fa0067c08d.png'/>
  </div>

Inicialmente, foi definido um saldo de R$1000,00 para o usuário, e, a partir disso, ele pode realizar saques, depósitos e PIX, contanto que o valor esteja disponível para tal.
Existem algumas regras no banco:

1.Depósitos são ilimitados.
2.É possível realizar 3 saques por dia, sendo que o valor não pode ultrapassar R$500,00 por saque.

## Validações
Existem algumas funções de validações principais no programa, sendo elas:

  ### Validação do valor digitado pelo usuário nos saques, depósito e PIX:
``` py
def validação_do_valor(valor):
    valor = float(valor)
    while (valor <= 0):
        valor = float(input('Valor inválido, por favor, digite um valor válido: '))
    return valor
```
  ### Validação do valor máximo do saque
  ### Validações do PIX:
Cada tipo de chave possuí um tipo de validação, ainda que de forma rudimentar.
O CPF possuí como validação ser necessário ter 11 caracteres, sendo eles numerais somente.
O possuí como validação ser necessário ter 10 caracteres, sendo eles numerais somente.
Para o email, é necessário ter 1 @ e 1 .com

Eis um exemplo
```
def checa_celular(celular):
    é_celular = celular.isdigit()
    while (len(celular) != 10 or é_celular == False):
        celular = input('Digite um celular válido!: ')
        é_celular = celular.isdigit()

    valor = input('Digite o valor do PIX: ')
    valor = validação_do_valor(valor)
    verifica_saldo_pix(valor)
```

