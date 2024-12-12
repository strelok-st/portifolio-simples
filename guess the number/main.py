# importando os módulos
import random;

# definindo as variáveis
global x;
global y;
global d;

# definindo as funções
def menu():
	menu = input(print(
		"""
		Oi, eu sou o jogo "Adivinhe o número". Selecione uma das opções abaixo digitando o número e pressionando "Enter":
		1) Comece o jogo
		2) Sair
		"""
		));
	if menu == "1":
		comece_jogo();
	else:
		quit();


def gere_numero():
	x = random.randint(0, 100);
	return x;

def comece_jogo():
	gere_numero();
	avalie_numero();

def avalie_numero(x, y, d):
	while True:
		y = input("Digite um número: ");
		y = int(y);
		if x > y:
			d = x - y;
			if 1 <= d <= 10:
				print("Pelando! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 11 <= d <= 20:
				print("Muito quente! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 21 <= d <= 30:
				print("Bem quente! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 31 <= d <= 40:
				print("Ficando quente! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 41 <= d <= 50:
				print("Morno! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 51 <= d <= 60:
				print("Ficando gelado! Quer tentar de novo?")
				avalie_numero(x, y, d);
			elif 61 <= d <= 70:
				print("Gelado! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 71 <= d <= 80:
				print("Frio! Quer tentar de novo?")
				avalie_numero(x, y, d);
			elif 81 <= d <= 90:
				print("Muito frio! Quer tentar de novo?")
				avalie_numero(x, y, d);
		elif x == y:
			d = x;
			print(f"Parabéns, {d} é o número correto! ");
			menu();
		elif x < y:
			d = y - x;
			if 1 <= d <= 10:
				print("Pelando! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 11 <= d <= 20:
				print("Muito quente! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 21 <= d <= 30:
				print("Bem quente! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 31 <= d <= 40:
				print("Ficando quente! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 41 <= d <= 50:
				print("Morno! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 51 <= d <= 60:
				print("Ficando gelado! Quer tentar de novo?")
				avalie_numero(x, y, d);
			elif 61 <= d <= 70:
				print("Gelado! Quer tentar de novo?");
				avalie_numero(x, y, d);
			elif 71 <= d <= 80:
				print("Frio! Quer tentar de novo?")
				avalie_numero(x, y, d);
			elif 81 <= d <= 90:
				print("Muito frio! Quer tentar de novo?")
				avalie_numero(x, y, d);

menu(); # começa o programa

# final do programa;