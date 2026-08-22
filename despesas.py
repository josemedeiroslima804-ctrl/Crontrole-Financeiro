from dataclasses import dataclass, field
from datetime import date

@dataclass
class Despesa:
    nome:str
    categoria: str
    valor: float
    data: date =field(default_factory=date.today)

    def __post_init__(self):
        if self.valor < 0 :
            raise ValueError ("O valor da despesa não pode ser negativo.")


    def __repr__(self):
        data_formatada = self.data.strftime("%d/%m/%Y")
        return f"<Despesa: {self.nome}, {self.categoria}, R${self.valor:.2f}, {data_formatada}>"