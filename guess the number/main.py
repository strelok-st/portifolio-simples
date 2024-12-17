# importando as bibliotecas
import random

def avalie_numero(x):
    while True:
        try:
            y = int(input("Digite um número (ou 'q' para sair): "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        if x == y:
            print(f"Parabéns, {x} é o número correto!")
            break  # Sai do loop
        
                d = abs(x - y)

        if d <= 10:
            print("Pelando! Quer tentar de novo?")
        elif d <= 20:
            print("Muito quente! Quer tentar de novo?")
        elif d <= 30:
            print("Bem quente! Quer tentar de novo?")
        elif d <= 40:
            print("Ficando quente! Quer tentar de novo?")
        elif d <= 50:
            print("Morno! Quer tentar de novo?")
        elif d <= 60:
            print("Ficando gelado! Quer tentar de novo?")
        elif d <= 70:
            print("Gelado! Quer tentar de novo?")
        elif d <= 80:
            print("Frio! Quer tentar de novo?")
        else:
            print("Muito frio! Quer tentar de novo?")

# gerando o número da vez;
while True: 
	lista = range(1,101);
	x = random.choice(lista);
	def menu():
		escolha = input("1) começa o jogo, 2) sai do jogo")
		if escolha == "1":
			avalie_numero(x);
		else:
			quit();
	menu();