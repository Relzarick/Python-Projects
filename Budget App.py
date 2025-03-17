from itertools import zip_longest
import math

class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.initial = False
        self.total = 0
        self.withdrawals = 0

    #! Use dictionaries for structured data
    #TODO some of the amount is not 2 decimal places (maybe change it to int and decimal magic first???)
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
            self.deposit(amt, "Initial deposit")
            self.initial = True
        elif transfer:
            self.deposit(amt, f"Transfer from {description}")
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
foods = Category('Clothing')
auto = Category('auto')



auto.deposit(1000, 'deposiT') 

#TODO something wrong with how the percentages are calc?????? 🗿

food.deposit(900, 'deposit')
food.withdraw(405.67, 'milk, cereal, eggs, bacon, bread')
food.transfer(1000, auto)



print(food)
print(auto)


cat_list = [food, auto, foods]


def create_spend_chart(categories):
    output_str = ''
    output_str += 'Percentage spent by category\n'

    category_names = [name.category for name in categories]
    withdrawal = [val.withdrawals for val in categories]
    total = [val.total for val in categories]

    percentages = [math.floor((w / t) * 100 / 10) * 10 if t else 0 for w, t in zip(withdrawal, total)]
    # print(percentages)

    #* Starting from 100 to 0 in 10s
    for level in range(100, -1, -10):
        #* :>3 is to right align it (no need for \n because its looping)
        line = f'{level:>3}|'

        for per in percentages:
            #* [20, 100, 0] if matches add 0 
            if per >= level:
                line += ' o '
            else:
                line += '   '

        output_str += f'{line}\n'
    
    #* Each name gets 3 '-' + 1 for spacing
    dashes = '-' * (len(category_names) * 3 + 1)
    output_str += f"    {dashes}\n"
    
    #* Iterates the longest, fills shorter with ''||* operator unpacks the names
    for row in zip_longest(*category_names, fillvalue=" "):
        #* This is to indent the names
        output_str += "     "
        output_str += f"{'  '.join(row)}\n"
    
    output_str.rstrip()
    print(output_str)

create_spend_chart(cat_list)


#! legacy code
#? :>2 is the f-str alignment(align right)
#? percent = ' '.join([f'{str(num):>2}|\n' for num in range(100, -1, -10)])