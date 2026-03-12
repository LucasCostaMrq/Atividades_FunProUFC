# Programa 3
# Escreva um programa que receba duas notas e seus respectivos pesos, calcule e mostre a média ponderada.

# Primeiro passo: Definir as variáveis
notaUm = float(input("Digite a primeira nota: "))
notaDois = float(input("Digite a segunda nota: "))
pesoUm = int(input("Digite o peso da primeira nota: "))
pesoDois = int(input("Digite o peso da segunda nota: "))

# Segundo Passo: definir restrições
# Uma nota não pode ser maior que 10 ou menor que 0
if (notaUm < 0 or notaDois < 0) or (notaUm > 10 or notaDois > 10 ):
    print("\nValor invalido para, pelo menos, uma das notas.")
    print("Insira valores entre 0 e 10.")
else:
     # Terceiro Passo: realize as operações
    mediaPond = ((notaUm * pesoUm) + (notaDois * pesoDois))/(pesoUm+pesoDois)

    # Quarto Passo: exiba os resultados
    print("\nA média ponderada resultou em: " , mediaPond)