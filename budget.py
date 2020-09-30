class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    # Method to deposit funds
    def deposit(self, amount, description=''):
        selfdep = {}
        selfdep['amount'] = amount
        selfdep['description'] = description
        self.ledger.append(selfdep)

    # Method to withdraw funds
    def withdraw(self, amount, description=''):
        spent = 0
        if self.check_funds(amount) == True:
            selfwith = {}
            selfwith['amount'] = amount * -1
            selfwith['description'] = description
            spent += amount
            self.ledger.append(selfwith)
            return True
        else:
            return False

    # Method to get balance
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance

    # Mthod to transfer balance
    def transfer(self, amount, category):
        category = category
        if self.check_funds(amount) == True:
            self.withdraw(float(amount), f'Transfer to {category.category}')
            category.deposit(float(amount), f'Transfer from {self.category}')
            return True
        else:
            return False

    # Check Funds
    def check_funds(self, amount):
        balance = 0
        balance = self.get_balance()
        if amount > float(balance):
            return False
        else:
            return True

    # Print Result
    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + \
            f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return output


def create_spend_chart(categories):
    total = 0
    withs = []
    cat = []
    percentage = []

    for name in categories:
        cat.append(name.category)
        spent = 0
        for w in name.ledger:
            if w['amount'] < 0:
                spent += w['amount']
        withs.append(spent)
    total = sum(withs)
    for idx in withs:
        percent = (idx / total) * 100
        percentage.append(percent)
    dlen = len(cat)
    title = 'Percentage spent by category' + '\n'
    longest = len(max(cat, key=len))
    for n in cat:
        cat[cat.index(n)] = n.ljust(longest)
    graph = ""
    names = '     '
    for i in range(0, longest):
        for pos in cat:
            names += pos[i] + '  '
        names += '\n     '

    for i in range(100, -10, -10):
        bar = " "
        line = str(i).rjust(3) + "|"

        #Add o if percent spending reaches there, spaces otherwise
        for percent in percentage:
            if percent >= i:
                bar += "o  "
            else:
                bar += "   "
        line += bar
        dashes = '    ' + ('-' * (dlen * 3)) + '-' + '\n'
        graph += line + "\n"

        output = title + graph + dashes + names.rstrip().rstrip('\n') + '  '
    return output
