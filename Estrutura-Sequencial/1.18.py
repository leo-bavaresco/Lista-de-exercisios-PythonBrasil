# Solicita o tamanho do arquivo em MB
arquivo = float(input('Informe o tamanho do Arquivo em MB: '))

# Solicita a velocidade do link de Internet em Mbps
velocidade_mb = float(input('Informe a velocidade na Internet em Mbps: '))

# Converte a velocidade para MB por segundo
velocidade_mb = velocidade_mb/8 # Convertendo de Mbps para MBps

# Calcula o tempo aproximado de download em segundos
download_segundos = arquivo / velocidade_mb

# Converte o tempo para minutos
download_minuto = download_segundos / 60

# Exibe o resultado
print (f"O tempo de download é de aproximadamente de: {download_minuto:2f} minutos ")