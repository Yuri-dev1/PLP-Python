prato = 30.00
bebida = 8.00
sobremesa = 12.00

qtd_prato = int(input("Digite a quantidade de pratos: "))
qtd_bebida = int(input("Digite a quantidade de bebidas: "))
qtd_sobremesa = int(input("Digite a quantidade de sobremesas: "))

subtotal_prato = prato * qtd_prato
subtotal_bebida = bebida * qtd_bebida
subtotal_sobremesa = sobremesa * qtd_sobremesa

subtotal = subtotal_prato + subtotal_bebida + subtotal_sobremesa

taxa = subtotal * 0.10

total = subtotal + taxa

pessoas = int(input("Digite em quantas pessoas será dividida a conta: "))

valor_por_pessoa = total / pessoas

print("\n===== CONTA =====")
print(f"Subtotal dos pratos: R$ {subtotal_prato:.2f}")
print(f"Subtotal das bebidas: R$ {subtotal_bebida:.2f}")
print(f"Subtotal das sobremesas: R$ {subtotal_sobremesa:.2f}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Taxa de serviço: R$ {taxa:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Valor por pessoa: R$ {valor_por_pessoa:.2f}")