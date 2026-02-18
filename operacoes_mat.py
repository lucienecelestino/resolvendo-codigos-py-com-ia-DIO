# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

numero1 = float(input("Digite o Primeiro Número:"))
numero2 = float(input("Digite o Segundo Número:"))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == "+":
    print("A soma dos números é:", numero1 + numero2)
elif operacao == "-":
    print("A subtração do número 1 pelo número 2 é:", abs(numero1 - numero2))
elif operacao == "*":
    print("A multiplicação dos números é:", numero1 * numero2)
elif operacao == "/":
    print("A divisão do número 1 pelo número 2 é:", numero1 / numero2)
else:
    print("Operação inválida!")
