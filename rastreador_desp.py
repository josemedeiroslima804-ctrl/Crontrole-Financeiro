from despesas import Despesas

def main():
    print("Rastreador de Despesas ativado!")

    despesa_file_path = "despesas.csv"
    carteira = 2000

    resumindo_despesas(despesa_file_path, carteira)


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
   



def resumindo_despesas(despesa_file_path, carteira):
    print(f"resumindo despesas")

    despesas = []

    with open(despesa_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            despesa_nome, despesa_valor, despesa_categoria = stripped_line.split(",")
            linha_despesa = Despesas(nome=despesa_nome, valor=float(despesa_valor), categoria=despesa_categoria)
            despesas.append(linha_despesa)


    valor_por_categoria = {}
    for despesa in despesas:
        key = despesa.categoria
        if key in valor_por_categoria:
            valor_por_categoria[key] += despesa.valor
        else:
            valor_por_categoria[key] = despesa.valor

    for key, valor in valor_por_categoria.items():
        print(f" {key}: R${valor:.2f}")


    despesas_totais = sum(x.despesas for x in despesas)
    print(f"suas despesas foram dê: R${despesas_totais:.2f} nesse mês !!")

    saldo_restante = carteira - despesas_totais
    print(f"saldo restante: R${saldo_restante:.2f}")




    




if __name__ == "__main__":
    main()