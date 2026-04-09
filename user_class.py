# CB 1st User Class

class User:
    def __init__(self,password,expenses_path,incomes_path,savings_path,currency):
        self.password = password
        self.expenses_path = expenses_path
        self.incomes_path = incomes_path
        self.savings_path = savings_path
        self.currency = currency