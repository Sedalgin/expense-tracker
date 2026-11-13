class Expense:
    def __init__(self,category,amount):
        self.category = category
        self.amount = amount


    def get_expense_1(self):
        return f"{self.category} = {self.amount} грн"

    def is_large(self,min_amount):
        return True if self.amount >= min_amount else False

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self,new_amount):
        if new_amount <= 0:
            raise ValueError("Сумма должна біть больше нуля")

        self._amount = new_amount

    def change_amount(self,new_amount):
        self.amount = new_amount

    def to_dict(self):
        slovar = {}
        slovar["Расходи"] = self.category
        slovar["Сумма"] = self.amount
        return slovar