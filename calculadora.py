# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def obter_numero(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")


def exibir_menu():
    print("\n" + "=" * 30)
    print("      CALCULADORA EM PYTHON")
    print("=" * 30)
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("0 - Sair")
    print("=" * 30)


def calculadora():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0-4): ").strip()

        if opcao == "0":
            print("\nEncerrando a calculadora. Até logo!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("\nOpção inválida! Escolha um número entre 0 e 4.")
            continue

        print("\n--- Entrada de Dados ---")
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        if opcao == "1":
            resultado = num1 + num2
            print(f"\nResultado: {num1} + {num2} = {resultado}")

        elif opcao == "2":
            resultado = num1 - num2
            print(f"\nResultado: {num1} - {num2} = {resultado}")

        elif opcao == "3":
            resultado = num1 * num2
            print(f"\nResultado: {num1} * {num2} = {resultado}")

        elif opcao == "4":
            if num2 == 0:
                print("\nErro: Não é possível realizar divisão por zero!")
            else:
                resultado = num1 / num2
                print(f"\nResultado: {num1} / {num2} = {resultado:.2f}")


if __name__ == "__main__":
    calculadora()
