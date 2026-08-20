class Despesas:
    def __init__(self, nome, categoria, valor) -> None:
        self.nome = nome
        self.categoria = categoria
        self.valor = valor


    def __repr__(self):
        return f"< Despesas: {self.nome}, {self.categoria}, R${self.valor:.2f} >"