## :file_folder: Programa em python de gerenciamento de valores de um banco

## Objetivos
O objetivo desse programa é estudar acerca de funções, variaveis globais, validações de strings e números, operadores e estruturas condicionais.

## O programa
O programa possui inicialmente um menu, com escolhas enumeradas de 1 a 5.

<div align=center>
  <img  width=400 src= 'https://user-images.githubusercontent.com/56310579/198419444-56ba73c0-b015-421a-917a-12fa0067c08d.png'/>
  </div>

Foi definido que o usuário tem um saldo inicial de R$1000,00.
A cada operação realizada, isto é, seja com um depósito, um saque ou PIX. o saldo irá se atualizar. Além disso, por fim, na opção de extrato, é exibida todas as operações realizadas anteriormente, assim como o saldo final.

## Depósito :inbox_tray:
É pedido um valor do depósito, que se estiver correto após a validação, isto é, não ser um valor não numérico e ou negativo, é exibido uma mensagem de sucesso. Após, é possível realizar novos depósitos, ou escolher entre retornar ao menu principal ou encerrar o programa.

<div align=center>
<img width=400 src='https://user-images.githubusercontent.com/56310579/198707432-1f1c3b03-288a-4ea5-99da-9fed7a719685.png'/>
</div>

## Saque :outbox_tray:
É pedido um valor de saque, no qual há um limite de 3 saques diários, no valor máximo de R$500,00 cada. A cada saque, é validado se o valor disponível em conta é suficiente para retirada do saque. Caso não, é exibida uma mensagem, informando o saldo atual, e se a pessoa deseja tentar realizar um novo saque.

<div align=center>
<img width=400 src='https://user-images.githubusercontent.com/56310579/198709519-28b58b77-7b27-4129-a2f6-95577e3d5fb9.png'/>
</div>

## Pix :money_with_wings:
