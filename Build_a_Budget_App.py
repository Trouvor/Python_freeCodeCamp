class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    def deposit(self, amount, description=""):
        self.ledger.append({'amount':amount, 'description': description})

    def withdraw(self, amount, description=""):        
        if self.check_funds(amount) :
            self.ledger.append({'amount':-amount, 'description': description})
            return True
        else :
          return False
    
    def get_balance(self):
        result = sum(x['amount'] for x in self.ledger)
        return result
    
    def transfer(self, amount, category):
        description = f'Transfer to {category.name}'
        result = self.withdraw(amount, description)

        if result :
            description = f'Transfer from {self.name}'
            category.deposit(amount, description)

        return result

    def check_funds(self, amount):
        return (self.get_balance() >= amount)

    def __str__(self):
        len_star = (30 - len(self.name)) // 2
        len_add = 30 - len(self.name) - (len_star * 2)
        title = "*" * len_star + self.name + "*" * (len_star + len_add)
        ledger_list = ""
        balance = 0
        for row_ledger in self.ledger:
            descr = row_ledger['description'][:23]
            amo_number = row_ledger['amount']
            ledger_list += f"\n{descr:<23}{amo_number:>7.2f}"
            balance = balance + amo_number

        return f"{title}{ledger_list}\nTotal: {balance:.2f}" 


def create_spend_chart(categories):
    total_spent = 0
    category_spent = []

    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spent.append(spent)
        total_spent += spent

    percentages = [int((spent / total_spent) * 100 // 10) * 10 for spent in category_spent]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_name_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_name_length) for category in categories]

    for i in range(max_name_length):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        chart += "\n"

    return chart.rstrip("\n")