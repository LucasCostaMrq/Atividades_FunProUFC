# Programa 4
# Escreva um programa que calcule e mostre a área de um círculo. Sabe-se que área = π*R².

# Import de uma biblioteca importante que contém o valor exato de pi
import math

# Primeiro passo: Definir as variáveis
raio = float(input("Digite o valor do raio do círculo: "))

# Segundo Passo: realize as operações
areaCir = math.pi * (raio * raio) # raio x raio = (raio)^2

# Terceiro Passo: exiba os resultados
print(f"\nA área do círculo resultou em: {areaCir:.4f}u") # formatado para 4 casa decimais