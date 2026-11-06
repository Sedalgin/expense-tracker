class Expense:
    def __init__(self,category,amount):
        self.category = category
        self.change_amount(amount)


    def get_expense_1(self):
        return f"{self.category} = {self.amount} грн"

    def is_large(self,min_amount):
        if self.amount >= min_amount:
            return True
        else:
            return False

    def change_amount(self,new_amount):
        if new_amount <= 0:
            raise ValueError("Сумма должна біть больше нуля")
        else:
            self.amount = new_amount


first_expense = Expense("Eда", 300)

second_expense = Expense("Такси", 100)

if __name__ == "__main__":
    print(first_expense.get_expense_1())
    print(second_expense.get_expense_1())
    print(first_expense.is_large(100))
    print(second_expense.is_large(150))