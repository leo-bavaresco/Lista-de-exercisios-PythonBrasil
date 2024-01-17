metros_quadrados = float(input('Informe os metros quadrados: '))

litro_lata = 18
cobertura_litro = 3
preco_lata = 80

litro_necessario = metros_quadrados / cobertura_litro

qtd_lata = litro_necessario/litro_lata

preco_final = qtd_lata*preco_lata

print (f'Sera necessario {qtd_lata} latas e custara {preco_final}')