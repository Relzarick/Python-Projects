from itertools import zip_longest

class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.initial = False
        self.total = 0
        self.withdrawals = 0

    #! Use dictionaries for structured data
    def __str__(self):
        ledger_str = f'{self.category.center(30, "*")}\n'

        for i in range(len(self.ledger)):
            #* justify both direction to ensure correct spacing
            description = self.ledger[i]['description'][:23].ljust(23)
            amount = f'{self.ledger[i]["amount"]}'.rjust(7)
            ledger_str += f'{description}{amount}\n'
        ledger_str += f'Total: {self.total}\n'
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
            self.withdrawals += amt
            return True
        else:
            return False
    

    def get_balance(self):
        print(self.total)


    def transfer(self, amt, category):
        if self.check_funds(amt):
            #* category.category to access target avoids the *
            self.ledger.append({'amount': f'-{amt}', 'description': f'Transfer to {category.category}'})
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
foods = Category('Foods')
niers = Category('niers')

food.deposit(10000, 'deposit')
food.transfer(1000, niers)
food.withdraw(4000, '123456')
niers.withdraw(1, 'niy')

# food.get_balance()

# print(food)
# print(niers)



#todo only calc withdrawals (denote with 0)
#TODO round down nearest 10
cat_list = [food, niers, foods]


def create_spend_chart(categories):
    output_str = ''
    output_str += 'Percentage spent by category\n'

    category_names = [name.category for name in cat_list]
    amount = [val.withdrawals for val in cat_list]

    #? :>2 is the f-str alignment(align right)
    percent = ' '.join([f'{str(num):>2}|\n' for num in range(100, -1, -10)])
    output_str += percent
    
    #* Each name gets 3 '-' + 1 for spacing
    dashes = '-' * (len(category_names) * 3 + 1)
    output_str += f"    {dashes}\n"
    
    
    #* Iterates the longest, fills shorter with ''
    #* * operator unpacks the names
    for row in zip_longest(*category_names, fillvalue=" "):
        #* This is to indent the names
        output_str += "     "
        output_str += f"{'  '.join(row)}\n"
        
    
    print(output_str)

create_spend_chart(cat_list)