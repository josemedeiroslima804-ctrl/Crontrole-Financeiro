from dataclasses import dataclass

@dataclass
class Despesa:
    nome:str
    categoria: str
    valor: float

def __post_int__(self):


    def __repr__(self):
        return f"<Despesas: {self.nome}, {self.categoria}, R${self.valor:.2f}>"