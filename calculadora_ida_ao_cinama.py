ingresso = 30.00
pipoca = 20.00
refrigerante = 10.00

qtd_ingresso = int(input("Quantidade de ingressos: "))
qtd_meia = int(input("Quantidade de meias-entradas: "))
qtd_pipoca = int(input("Quantidade de pipocas: "))
qtd_refrigerante = int(input("Quantidade de refrigerantes: "))

pessoas = int(input("Entre quantas pessoas será dividido? "))

subtotal_ingresso = qtd_ingresso * ingresso
desconto_meia = qtd_meia * (ingresso / 2)
subtotal_ingresso -= desconto_meia

subtotal_pipoca = qtd_pipoca * pipoca
subtotal_refrigerante = qtd_refrigerante * refrigerante

total = subtotal_ingresso + subtotal_pipoca + subtotal_refrigerante

combo = qtd_pipoca >= 1 and qtd_refrigerante >= 1

if combo:
    total -= 5.00

taxa = total * 0.05
total += taxa

valor_pessoa = total / pessoas

passeio_caro = valor_pessoa > 40.00

print("\n========== RECIBO ==========")
print(f"Ingressos:        R$ {subtotal_ingresso:.2f}")
print(f"Pipocas:          R$ {subtotal_pipoca:.2f}")
print(f"Refrigerantes:    R$ {subtotal_refrigerante:.2f}")
print(f"Taxa:             R$ {taxa:.2f}")
print(f"Total:            R$ {total:.2f}")
print(f"Por pessoa:       R$ {valor_pessoa:.2f}")
print(f"Passeio saiu caro? {passeio_caro}")
print("============================")