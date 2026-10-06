def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b


while True:
    print("\n===== CALCULADORA =====")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Obrigado por usar a calculadora. Até mais!")
        break

    elif opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = somar(numero1, numero2)
                print(f"Resultado: {resultado}")

            elif opcao == "2":
                resultado = subtrair(numero1, numero2)
                print(f"Resultado: {resultado}")

            elif opcao == "3":
                resultado = multiplicar(numero1, numero2)
                print(f"Resultado: {resultado}")

            elif opcao == "4":
                if numero2 == 0:
                    print("Erro: Divisão por zero não é permitida")
                else:
                    resultado = dividir(numero1, numero2)
                    print(f"Resultado: {resultado}")

        except ValueError:
            print("Erro: digite apenas números válidos.")

    else:
        print("Erro: opção inválida. Escolha uma opção de 1 a 5.")
