import math
# Solicita o tamanho da área a ser pintada em metros quadrados
area_pintada = float(input("Informe o tamanho da area em m²: "))


# Define a cobertura da tinta em metros quadrados por litro
cobertura_por_litro = 6


# Define os tamanhos de lata e galão, e os preços correspondentes
tamanho_lata = 18
preco_lata = 80

tamanho_galao = 3.6
preco_galao = 25


# Calcula a quantidade de litros necessários com 10% de folga
litro_necessario = area_pintada/cobertura_por_litro * 1.1


# Calcula a quantidade de latas necessárias
qtd_lata = math.ceil(litro_necessario/tamanho_lata)


# Calcula o preço total ao comprar apenas latas
preco_total_lata = qtd_lata * preco_lata


# Calcula a quantidade de galões necessários
qtd_galao = math.ceil(litro_necessario*preco_galao)


# Calcula o preço total ao comprar apenas galões
preco_total_galao = qtd_galao * preco_galao


# Calcula a quantidade de latas e galões misturados para minimizar o desperdício
quantidade_latas_misturadas = math.floor(litro_necessario / tamanho_lata)
litros_restantes = litro_necessario % tamanho_lata
quantidade_galoes_misturados = math.ceil(litros_restantes / tamanho_galao)


# Calcula o preço total ao misturar latas e galões
preco_total_misturado = (quantidade_latas_misturadas * preco_lata) + (quantidade_galoes_misturados * preco_galao)


# Exibe os resultados
print(f"Situação 1 - Comprar apenas latas de 18 litros:")
print(f"Quantidade de latas necessárias: {qtd_lata}")
print(f"Preço total: R$ {preco_total_lata:.2f}\n")

print(f"Situação 2 - Comprar apenas galões de 3,6 litros:")
print(f"Quantidade de galões necessários: {qtd_galao}")
print(f"Preço total: R$ {preco_total_galao:.2f}\n")

print(f"Situação 3 - Misturar latas e galões para minimizar o desperdício:")
print(f"Quantidade de latas necessárias: {quantidade_latas_misturadas}")
print(f"Quantidade de galões necessários: {quantidade_galoes_misturados}")
print(f"Preço total: R$ {preco_total_misturado:.2f}")