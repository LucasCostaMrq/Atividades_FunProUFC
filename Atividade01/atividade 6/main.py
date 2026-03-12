# Programa 6
# Escreva um programa que pede os seguintes dados:
# - Valor do salário de um funcionário.
# - Aumento em porcentagem.
# - Mostre o valor do aumento e o salário com aumento.

# Primeiro passo: Definir as variáveis
salario =  float(input("Digite o valor do salário: "))
aumentoPerCent = float(input("Digite o valor do aumento em porcentagem: "))

# Segundo Passo: faças as operações
valorAumento = salario * (aumentoPerCent/100)
salarioPosAumento = salario + valorAumento

# Terceiro Passo: exibir as informações
print("\nO valor de acrécimo é: ", valorAumento)
print("O salário após o aumento resultou em: ", salarioPosAumento)