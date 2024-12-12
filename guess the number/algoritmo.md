## menu
1. faça o programa imprimir a mensagem: 
"""
Oi, eu sou o jogo "Adivinhe o número". Selecione uma das opções abaixo digitando o número e pressionando "Enter":
1) Comece o jogo
2) Sair

"""

## gere_numero (retorna x)
1. importe a função random
2. associe o comando random.randint(0, 100) a uma variável
3. retorne essa variável para o programa

## comece_jogo 
1. chama a função gere_numero;
2. chama a função avaliadora;
3. chama a função menu_2;

## avalie_numero (x, y, d)
1. recebe os valores
2. se x = d, imprime "Parabéns! Você acertou!" e volta ao menu principal;
3. se x > y, faz x - y e avalia a condição relativa à distância;
4. se y > x, faz y - x e avalia a condição relativa à distância;
