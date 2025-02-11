class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []
  
  def __str__(self):
    result = []
    result.append(self.category.center(30, "*"))
    for item in self.ledger:
      result.append(f"{item['description'][:23]:<23}{item['amount']:>7.2f}")
    result.append(f"Total: {self.get_balance()}")
    return '\n'.join(result)

  def get_balance(self):
    balance = 0
    if not self.ledger:
      return balance
    else:
      for item in self.ledger:
        balance += item['amount']
      return balance

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  def deposit(self, amount, description = ''):
    self.ledger.append({'amount':amount, 'description':description})

  def withdraw(self, amount, description = ''):
    if amount > self.get_balance():
      return False
    else:
      self.ledger.append({'amount':amount * -1, 'description':description})
      return True
    
  def transfer(self, amount, other_categoryy):
    if amount > self.get_balance():
      return False
    else:
      self.withdraw(amount, f'Transfer to {other_categoryy.category}')
      other_categoryy.deposit(amount, f'Transfer from {self.category}')
      return True

def create_spend_chart(categories):
    # Calculate total spending per category
    total_spent = []
    total_spent_all = 0
  
    for category in categories:
      for item in category.ledger:
          if item['amount'] < 0:
              total_spent_all += abs(item['amount'])
    
    for category in categories:
        spent = sum(abs(item['amount']) for item in category.ledger if item['amount'] < 0)
        total_spent.append((category.category, spent))

    # Convert spending into percentages rounded down to nearest 10
    percentages = [(name, (spent / total_spent_all) * 100) for name, spent in total_spent]
    percentages = [(name, int(percent // 10) * 10) for name, percent in percentages]

    # Build the chart output
    output = "Percentage spent by category\n"

    # Print the percentage scale (100 down to 0)
    for i in range(100, -10, -10):
        line = f"{i:>3}| "
        for _, percent in percentages:
            line += "o  " if percent >= i else "   "
        output += line + "\n"

    # Add dashed line correctly aligned
    output += "    " + "-" * (len(percentages) * 3 + 1) + "\n"

    # Print category names vertically
    max_name_length = max(len(name) for name, _ in percentages)
    category_names = [name for name, _ in percentages]

    for i in range(max_name_length):
        line = "     "
        for name in category_names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        output += line
        if i < max_name_length - 1:  # Avoid adding an extra newline at the end
            output += "\n"
    return output


food = Category('Food')
food.deposit(100, 'Grocery, Vegetables, Fish')
food.deposit(200, 'Coke, Chips, Biscuits')
food.withdraw(20, 'Taken money for tea')

clothing = Category('Clothing')
clothing.deposit(50, 'jeans')
clothing.deposit(30, 'shirt')
clothing.withdraw(50, 'Money for trouser')

food.transfer(70, clothing)

auto = Category('Auto')
auto.deposit(150, 'jeans')
auto.deposit(530, 'shirt')
auto.withdraw(300, 'Money for trouser')

print(food)
print('\n')
print(clothing)
print('\n')
print(auto)
print('\n')
print(create_spend_chart([food, clothing, auto]))