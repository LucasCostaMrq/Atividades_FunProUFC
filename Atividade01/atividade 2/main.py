# Programa 2
# Faça um programa que receba três notas, calcule e mostre a média aritmética

# Primeiro Passo: Definir as variáveis
notaUm = float(input("Digite a primeira nota: "))
notaDois = float(input("Digite a segunda nota: "))
notaTres = float(input("Digite a terceira nota: "))

# Segundo Passo: definir restrições
# Uma nota não pode ser maior que 10 ou menor que 0
if (notaUm < 0 or notaDois < 0 or notaTres < 0) or (notaUm > 10 or notaDois > 10 or notaTres > 10):
    print("\nValor invalido para, pelo menos, uma das notas.")
    print("Insira valores entre 0 e 10.")

else:
    # Terceiro Passo: realize as operações
    mediaAritmetica = (notaUm + notaDois + notaTres)/3

    # Quarto Passo: exiba os resultados
    print("\nA média aritmética resultou em: " , mediaAritmetica)



