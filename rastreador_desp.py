from despesas import Despesas

def main():
    print("Rastreador de Despesas ativado!")

    despesa_file_path = "despesas.csv"

    despesa = despesas_usuario()

    salvando_despesas(despesa, despesa_file_path)

    resumindo_despesas(despesa_file_path)


def despesas_usuario():
    print("Obtendo despesas...")

    nome_desp = input("Digite o nome da despesa: ")
    valor_desp = float(input("Digite o valor da despesa: "))

    categoria_desp = [
        "🍕 Comida",
        "🏠 Casa",
        "🥳 Lazer",
        "💼 Trabalho",
    ]

    while True:
        print("\nSelecione a categoria:")

        for i, categoria_nome in enumerate(categoria_desp):
            print(f"{i + 1}. {categoria_nome}")

        value_range = f"[1 - {len(categoria_desp)}]"

        try:
            select_index = int(
                input(f"Digite o número da categoria {value_range}: ")
            ) - 1

            if select_index in range(len(categoria_desp)):
                categoria_selecionada = categoria_desp[select_index]

                nova_desp = Despesas(
                    nome=nome_desp,
                    categoria=categoria_selecionada,
                    valor=valor_desp
                )

                return nova_desp

            else:
                print("Categoria não encontrada. Tente novamente.")

        except ValueError:
            print("Digite apenas números.")


def salvando_despesas(despesa: Despesas, despesa_file_path):
    print(f"Salvando despesas {despesa} para {despesa_file_path}")

    with open(despesa_file_path, "a", encoding="utf-8", newline="") as f:
        f.write(f"{despesa.nome},{despesa.valor},{despesa.categoria}\n")
   



def resumindo_despesas(despesa_file_path):
    print(f"resumindo despesas")

    despesas = []

    with open(despesa_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()

    




if __name__ == "__main__":
    main()