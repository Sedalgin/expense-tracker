from dataclasses import dataclass

@dataclass
class StockItem:
    name:str
    quantity:int

    def __post_init__(self):
        if self.quantity < 0:
            raise ValueError("Остаток не может біть меньше ноля")

    def __str__(self):
        return f"{self.name} -- Остаток {self.quantity}"

    def sell(self,amount):
        if amount <= 0:
            raise ValueError(f"Число должно біть больше ноля")
        elif self.quantity < amount:
            raise ValueError (f"Осталось {self.quantity}")
        else:
            self.quantity -= amount
            return self.quantity

if __name__ == "__main__":
    x = StockItem("Stock Item",5)
    h = x
    h.quantity = 10
    print(x.quantity)