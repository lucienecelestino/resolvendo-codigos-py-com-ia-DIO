# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

texto = input("Digite um texto: ")
vezes = int(input("Digite o número de vezes que deseja repetir o texto: "))

texto_repetido = (texto + '\n') * vezes
print("O texto repetido é:\n", texto_repetido)