class StockItem:
    def __init__(self, name, quantity):
        self.name = name
        if quantity < 0:
            raise ValueError("Остаток не может біть меньше ноля")
        else:
            self.quantity = quantity

    def text(self):
        print(f"{self.name} -- Остаток {self.quantity}")

    def sell(self,amount):
        if amount <= 0:
            raise ValueError(f"Число должно біть больше ноля")
        elif self.quantity < amount:
            raise ValueError (f"Осталось {self.quantity}")
        else:
            self.quantity -= amount
            return self.quantity

if __name__ == "__main__":
    x = StockItem("Stock Item", 5)
    x.sell(4)
    x.text()