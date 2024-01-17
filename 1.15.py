salario_hora = float(input('Digite o salario por hora: '))
hora_trabalhada = float(input('Digite a quantidade de horas trabalhadas no mes: '))

salario_bruto = salario_hora * hora_trabalhada

inss = (11*salario_bruto)/100

sindicato = (5*salario_bruto)/100

imposto = (11*salario_bruto)/100

salario_liq = salario_bruto-(sindicato+inss+imposto)


print(f"O salario bruto desse mes é {salario_bruto:} reais")
print(f'Foi pago {imposto} reais de imposto de renda')
print(f'Foi pago {inss} rais de inss')
print(f'Foi pago {sindicato} reais de sindicato')
print(f'O salario liquido desse mes é {salario_liq} reais')

print(f""" 
================================
Salario Bruto: {salario_bruto}
Imposto de Renda 11%: {imposto}
Inss 11%: {inss}
Sindicato 5%: {sindicato}
Salario Liquido: {salario_liq}
================================
""")