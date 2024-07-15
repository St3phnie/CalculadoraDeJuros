print('Bem vindos a loja da Stephanie Marrocos')

# Pede para que o usuário informe o valor do pedido e quantidade de parcelas
valorDoPedido = float(input('Informe o valor do pedido: '))
quantidadeDeParcelas = int(input('Informe a quantidade de parcelas: '))

# Variável Juros
juros = 0

# Quantidade de juros se baseando na quantidade de parcelas
if quantidadeDeParcelas < 4:
    juros = 0
elif 4 <= quantidadeDeParcelas < 6:
    juros = 0.04
elif 6 >= quantidadeDeParcelas < 9:
    juros = 0.08
elif 9 >= quantidadeDeParcelas < 13:
    juros = 0.16
else:
    juros = 0.32

# Cálculo do valor da parcela e do valor total parcelado
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeDeParcelas
valorTotalParcelado = valorDaParcela * quantidadeDeParcelas

# Exibindo os resultados

print('O valor total das parcelas é de: R$', int(valorDaParcela * 100) / 100)
print('O valor total do pedido parcelado é de: R$', int(valorTotalParcelado * 100) / 100)
