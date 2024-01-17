opcao = input("Por favor, informe o sexo (digite 'homem' ou 'mulher'): ")
altura = float(input('Informe sua altura: '))

if opcao.lower() == 'homem':
    peso_ideal = (72.7*altura) - 58
else:
    peso_ideal = (62.1*altura) - 44.7

print(f"Seu peso ideal é: {peso_ideal:.2f} kg")