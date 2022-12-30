# Calculando o índice de massa corporal em python
import math

# Entrada de dados
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# Processamento
imc = peso / (math.pow(altura, 2))

# Saída de dados
print("O seu IMC é: %.2f" %imc)

if(imc < 18.5):
    print("Você está abaixo do peso.")
elif(imc >= 18.5 and imc < 25):
    print("Você está com o peso ideal.")
elif(imc >= 25 and imc < 30):
    print("Você está com sobrepeso.")
elif(imc >= 30 and imc < 40):
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbida.")
