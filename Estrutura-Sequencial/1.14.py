peso_peixe = float(input('Informe o peso do peixe: '))

peso_maximo = 50

if peso_peixe > peso_maximo:
    excesso = peso_peixe - peso_maximo
    multa = excesso * 4
    print (f'Infelizmente o peixe excedou o limete de peso e sera necessario pagar {multa:.2f} reais de multa')
else:
        print(f'Parabens, o peixe nao excedou o limite de peso')