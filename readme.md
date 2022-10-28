## :file_folder: Programa em python de gerenciamento de valores de um banco

## Objetivos
O objetivo desse programa é estudar acerca de funções, variaveis globais, validações de strings e números, operadores e estruturas condicionais.

## O programa
O programa possui inicialmente um menu, com escolhas enumeradas de 1 a 5.

<div align=center>
  <img  width=400 src= 'https://user-images.githubusercontent.com/56310579/198419444-56ba73c0-b015-421a-917a-12fa0067c08d.png'/>
  </div>

Foi definido que o usuário tem um saldo inicial de R$1000,00.
A cada operação realizada, isto é, seja com um depósito, um saque ou PIX, o saldo irá se atualizar. Além disso, na opção de extrato é exibida todas as operações realizadas anteriormente, assim como o saldo final.

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

É possível escolher dentre 4 opções, sendo elas CPF, celular, chave aleatória e email. Cada tipo de chave possui suas  respectivas verificações de validade dos dados, ainda que de forma simplificada.


Após escolher o tipo de chave, é requerido o valor, e, caso tudo ocorra certo, é exibida uma mensagem de sucesso.
Assim como no saque, o pix desconta dinheiro do seu saldo. Logo, há uma função que verifica se o saldo em conta é suficiente para realização do PIX.

<div align=center>
<img width=400 src='https://user-images.githubusercontent.com/56310579/198716674-9576ef01-f466-4040-94d1-35602fec6652.png'/>
</div>

## Extrato bancário :scroll:

Por fim, é possível exibir no extrato todas as operações realizadas enquanto o programa está ativo, listadas por valor e tipo de operação, além do saldo final da conta.
<div align=center>
<img width=400 src='https://user-images.githubusercontent.com/56310579/198723365-37e9e059-0d2b-4d47-96ca-604f10e98036.png'/>
</div>



