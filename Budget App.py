class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.initial = False
        self.total = 0


    def __str__(self):
        ledger_str = f'{self.category.center(30, '*')}\n'
        #Todo spacing between parems(limit desc to 23 chara)
        #TODO amt  use rjust, use float, max 7 chara
        for i in self.ledger:
            ledger_str += f'{i}\n'
        ledger_str += f'Total: {self.total}\n'
        return ledger_str

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


#TODO takes a list of cats
#TODO returns a string(bar chart)
#TODO round down nearest 10
#TODO cat name go vert down
#TODO title up top says (Percentage spent by category)
def create_spend_chart(categories):
    pass