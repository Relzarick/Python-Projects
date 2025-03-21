from itertools import zip_longest
import math

class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.initial = True
        self.total = 0
        self.withdrawals = 0

    #! Use dictionaries for structured data

    def __str__(self):
        ledger_str = f'{self.category.center(30, "*")}\n'

        for i in range(len(self.ledger)): # list
            #* justify both direction to ensure correct spacing
            amount = f'{float(self.ledger[i]["amount"]):.2f}'.rjust(7)
            #* length is used to determine length of description and padding
            length = 30 - len(amount)
            description = self.ledger[i]['description'][:23].ljust(length)
            
            ledger_str += f'{description}{amount}\n'
        ledger_str += f'Total: {round(self.total, 2)}'
        return ledger_str


    def deposit(self, amt, description = ''):
        if not self.initial and description.lower() == 'deposit':
            self.deposit(amt, "Initial deposit")
            self.initial = True
        else:
            self.ledger.append({'amount': amt, 'description': description})
            self.total += amt
        

    def withdraw(self, amt, description = ''):
        if self.check_funds(amt):
            self.ledger.append({'amount': -amt, 'description': description})
            self.total -= amt
            self.withdrawals += amt
            return True
        else:
            return False
    
    def get_balance(self):
        return self.total

    def transfer(self, amt, category):
        if self.check_funds(amt):
            #* category.category to access target avoids the *
            self.ledger.append({'amount': -amt, 'description': f'Transfer to {category.category}'})
            category.deposit(amt, f'Transfer from {self.category}')
            self.total -= amt
            return True
        else:
            return False


    def check_funds(self, amt):
        # if amt >= 10000:
        #     self.ledger.append({'amount': '0', 'description': "Over 10k's tough, bruv"})
        #     return False

        if amt > self.total:
            # self.ledger.append({'amount': '0', 'description': 'Not Enough Money Bruh'})
            return False
        else:
            return True

#! chart shows percentages of individual category based on total sum of withdrawal
def create_spend_chart(categories):
    output_str = ''
    output_str += 'Percentage spent by category\n'

    category_names = [name.category for name in categories]
    withdrawal = [val.withdrawals for val in categories]
    total = (lambda nums: sum(nums))(withdrawal)


    percentages = [math.floor((w / total) * 100 / 10) * 10 if total else 0 for w in withdrawal]
    
    # print(total) 
    # print(withdrawal)
    # print(percentages)

    #* Starting from 100 to 0 in 10s
    for level in range(100, -1, -10):
        #* :>3 is to right align it (no need for \n because its looping)
        line = f'{level:>3}|'

        #? index then start
        for i, per in enumerate(percentages):
            #* check if per meets or exceeds the level (62/60)
            if per >= level:
                line += ' o '
            else:
                #* This adds filler if there is no O
                line += '   '
                #* If last only add ONE space
            if i == len(percentages) - 1:
                line += ' ' 

        output_str += f'{line}\n'
    
    #* Each name gets 3 '-' + 1 for spacing
    dashes = '-' * (len(category_names) * 3 + 1)
    output_str += f"    {dashes}\n"
    

    #* Iterates the longest, fills shorter with ''||* operator unpacks the names
    for row in zip_longest(*category_names, fillvalue=" "):
        #* This adds indentation for the names
        output_str += "     "
        
        # print(row)
        #* Each row contains a tuple of the letters
        for i, chara in enumerate(row):
            #* If i is last, append -- 
            if i == len(row) - 1:  
                output_str += f"{chara}  "  
            else:
                #* This appends the spacing between letters
                output_str += f"{chara}  "

        #* Append \n after each row for formatting
        output_str = output_str + "\n"
    
    return output_str.rstrip('\n')
    # print(output_str.rstrip())
    # print(output_str.rstrip('--'))
    # print(output_str.rstrip() is output_str.rstrip('\n'))


food = Category('Food')
clothing = Category('Clothing')
auto = Category('auto')
la = Category('la')

auto.deposit(1000, 'deposit') 

food.deposit(2000, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
food.withdraw(1)

food.transfer(1000, auto)

clothing.deposit(8000, 'deposit')
clothing.withdraw(5500, 'niy')

print(food)
print(auto)
cat_list = [food,auto, la, clothing]

print(create_spend_chart(cat_list))
# create_spend_chart(cat_list)


#! legacy code
#? output_str += f"{'  '.join(row)}\n"
#? percentages = [math.floor((w / t) * 100 / 10) * 10 if t else 0 for w, t in zip(withdrawal, total)]
#? :>2 is the f-str alignment(align right)
#? percent = ' '.join([f'{str(num):>2}|\n' for num in range(100, -1, -10)])