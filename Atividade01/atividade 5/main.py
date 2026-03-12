# Programa 5
# Escreva um programa que recebe um número positivo e maior que zero, calcule emostre:
#a) O número digitado ao quadrado.
#b) O número digitado ao cubo.


# Primeiro passo: Definir as variáveis
valor = float(input("Digite um número: "))

# Segundo Passo: definir restrições
# Precisa ser um número positivo e maior que zero
if (valor <= 0):
    print("Valor inválido. Insira um valor maior que zero.")
else:
    # Terceiro Passo: realize as operações
    valorQuadrado = valor ** 2
    valorCubo = valor ** 3

    # Quarto Passo: exiba os resultados
    print("Valor ao quadrado: " , valorQuadrado)
    print("Valor ao cubo: " , valorCubo)
