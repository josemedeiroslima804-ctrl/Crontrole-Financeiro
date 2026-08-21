from despesas import Despesa

def main():
    print("Rastreador de Despesas ativado!")

    despesa_file_path = "despesas.csv"

    carteira = 2000

    despesa = obter_despesa

    salvar_despesa(despesa, despesa_file_path)

    mostra_resumo(despesa_file_path, carteira)


def obter_nome():
    desp_nome = input("Digite o nome da despesa: ")
    return desp_nome

def obter_valor():

    while True:
        try:
            desp_valor = float(input("Digite o valor da despesa: "))

            if desp_valor > 0:
                return desp_valor
            
            else:
                print("O valor deve ser maior que zero!")

        except ValueError:
            print("Digite apenas números.")


    

def obter_categoria():
    categorias = [
        "🍕 Comida",
        "🏠 Casa",
        "🥳 Lazer",
        "💼 Trabalho",
    ]

    while True:
            print("\nSelecione a categoria:")
    
            for i, categoria_nome in enumerate(categorias):
                print(f"{i + 1}. {categoria_nome}")
    
            value_range = f"[1 - {len(categorias)}]"
    
            try:
                select_index = int(
                    input(f"Digite o número da categoria {value_range}: ")
                ) - 1
    
                if select_index in range(len(categorias)):
                    categoria_selecionada = categorias[select_index]
                    return categoria_selecionada
    
    
                else:
                    print("Categoria não encontrada. Tente novamente.")
    
            except ValueError:
                print("Digite apenas números.")

               

def obter_despesa():
    nome = obter_nome()
    valor = obter_valor()
    categoria = obter_categoria()

    nova_desp = Despesa(
        nome=nome,
        valor=valor,
        categoria=categoria
    )

    return nova_desp
    



def salvar_despesa(despesa: Despesa, despesa_file_path):
    print(f"Salvando despesas {despesa} para {despesa_file_path}")

    with open(despesa_file_path, "a", encoding="utf-8", newline="") as f:
        f.write(f"{despesa.nome},{despesa.valor},{despesa.categoria}\n")
   



def mostra_resumo(despesa_file_path, carteira):
    print(f"resumindo despesas")

    despesas = []

    with open(despesa_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            despesa_nome, despesa_valor, despesa_categoria = stripped_line.split(",")
            linha_despesa = Despesa(nome=despesa_nome, valor=float(despesa_valor), categoria=despesa_categoria)
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


    despesas_totais = sum(x.valor for x in despesas)

    print(f"suas despesas foram dê: R${despesas_totais:.2f} nesse mês !!")

    saldo_restante = carteira - despesas_totais
    print(f"saldo restante: R${saldo_restante:.2f}")




    




if __name__ == "__main__":
    main()