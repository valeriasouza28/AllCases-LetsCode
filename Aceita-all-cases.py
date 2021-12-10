
#Objetivo: fazer pergunta ao usuário, enquanto nome for 'rio de janeiro', independente das caixas maiúsculas ou minúsculas estará correto. Caso o usuário digite um nome diferente, o programa pedirá para tentar de novo.

nome_cidade = input("Que cidade do Brasil é conhecida como cidade maravilhosa?")
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'rio de janeiro':
	print('Tenta de novo, vai')
	nome_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhosa?')
	
	
	print('Boa Campeã(o)')