# Programa 1
# Escreva um programa que pede os dados do usuário e mostra a ficha preenchida

# Primeiro passo: Definir as variáveis
nome = input("Digite seu nome: ")
matricula = input("Digite seu matricula: ")
curso = input("Digite seu curso: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu e-mail: ")

# Segundo Passo: exibir as variáveis
print(
    "\nFicha Preenchida!" \
    "\nNome: " + nome +
    "\nMatrícula: " + matricula + \
    "\nCurso: " + curso + \
    "\nIdade: " , idade , \
    "\nEmail: " + email
)