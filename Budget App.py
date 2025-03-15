class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.initial = False
        self.total = 0

    def __str__(self):
        ledger_str = f'{self.category}\n'
        for i in self.ledger:
            ledger_str += f'{i}\n'
        return ledger_str

    #Todo spacing between parems
    def deposit(self, amt, description = '', transfer = 0):
        if not self.initial and description.lower() == 'deposit':
            self.ledger.append(f'Initial {description} {amt}')
            self.initial = True
            self.total += amt
        elif transfer == 1:
            self.ledger.append(f'Transfer from {description} {amt}')
            self.total += amt
        else:
            self.ledger.append(f'{description} {amt}')
            self.total += amt
        

    def withdraw(self, amt, description):
        if self.check_funds(amt):
            self.ledger.append(f'{description} -{amt}')
            self.total -= amt
            return True
        else:
            return False
    
    def get_balance(self):
        print(self.total)

    def transfer(self, amt, category):
        if self.check_funds(amt):
            self.ledger.append(f'Transfer to {category.category} -{amt}')
            self.total -= amt
            category.deposit(amt, self.category, 1)
            return True
        else:
            return False

    def check_funds(self, amt):
        if amt > self.total:
            return False
        else:
            return True



food = Category('Food')
niers = Category('niers')

food.deposit(10000, 'deposit')
food.transfer(1000, niers)
food.withdraw(4000, 'nis')

# food.get_balance()

print(food)
print(niers)



def create_spend_chart(categories):
    pass