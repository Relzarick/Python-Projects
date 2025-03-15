class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.initial = False
        self.total = 0

    #! Use dictionaries for structured data
    
    def __str__(self):
        #! transfer is **** because of below
        ledger_str = f'{self.category.center(30, '*')}\n'

        for i in range(len(self.ledger)):
            #* justify both direction to ensure correct spacing
            description = self.ledger[i]['description'][:23].ljust(23)
            amount = f'{self.ledger[i]['amount']}'.rjust(7)
            ledger_str += f'{description}{amount}\n'
        return ledger_str


    def deposit(self, amt, description = '', transfer = False):
        if not self.initial and description.lower() == 'deposit':
            self.ledger.append({'amount': amt, 'description': f'Initial {description}'})
            self.initial = True
            self.total += amt
        elif transfer:
            self.ledger.append({'amount': amt, 'description': f'Transfer from {description}'})
            self.total += amt
        else:
            self.ledger.append({'amount': amt, 'description': description})
            self.total += amt
        

    def withdraw(self, amt, description):
        if self.check_funds(amt):
            self.ledger.append({'amount': f'-{amt}', 'description': description})
            self.total -= amt
            return True
        else:
            return False
    

    def get_balance(self):
        print(self.total)


    def transfer(self, amt, category):
        if self.check_funds(amt):
            self.ledger.append({'amount': f'-{amt}', 'description': f'Transfer to {category}'})
            category.deposit(amt, self.category, True)
            self.total -= amt
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
food.withdraw(4000, '12345678901234567890123456')

# food.get_balance()

print(food)
# print(niers)


#TODO takes a list of cats
#TODO returns a string(bar chart)
#TODO round down nearest 10
#TODO cat name go vert down
#TODO title up top says (Percentage spent by category)
def create_spend_chart(categories):
    pass