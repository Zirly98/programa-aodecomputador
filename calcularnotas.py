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
def obter_nota(ordem: int) -> float:
    """Solicita e valida uma nota entre 0.0 e 10.0."""
    while True:
        try:
            nota = float(input(f"Digite a nota N{ordem} (0.0 a 10.0): "))
            if 0.0 <= nota <= 10.0:
                return nota
            print("Entrada inválida: a nota deve estar entre 0.0 e 10.0.")
        except ValueError:
            print("Entrada inválida: digite apenas valores numéricos.")


def calcular_media_aluno():
    print("--- MÉDIA E STATUS DO ALUNO ---\n")

    n1 = obter_nota(1)
    n2 = obter_nota(2)
    n3 = obter_nota(3)
    n4 = obter_nota(4)

    media = (n1 + n2 + n3 + n4) / 4

    if media >= 7.0:
        status = "Aprovado"
    elif media >= 5.0:
        status = "Em Recuperação"
    else:
        status = "Reprovado"

    print("\n" + "=" * 35)
    print(f"Média final: {media:.2f}")
    print(f"Situação: {status}")
    print("=" * 35)


if __name__ == "__main__":
    calcular_media_aluno()
