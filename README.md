# Budget App (Python)

This is a Python-based Budget App that allows users to manage their expenses by categorizing transactions and visualizing spending. This project was a mandatory requirement to complete the **'Scientific Computing with Python'** certification on **FreeCodeCamp**.

## Features

- **Category Management**: Create budget categories such as `Food`, `Clothing`, and `Auto`.
- **Deposit Functionality**: Add money to a category with an optional description.
- **Withdrawal Functionality**: Withdraw money from a category with an optional description.
- **Transfer Funds**: Transfer money from one category to another.
- **Balance Checking**: Get the current balance of a category.
- **Check Funds Before Spending**: Ensure sufficient funds before making withdrawals.
- **Spending Visualization**: Generate a bar chart representing the percentage of total expenses per category.

## Implementation

The application consists of a `Category` class with the following methods:
- `__init__(category)`: Initializes a budget category with an empty ledger.
- `__str__()`: Returns a formatted string representation of the budget category, including transactions.
- `deposit(amount, description='')`: Adds funds to the category.
- `withdraw(amount, description='')`: Removes funds from the category if sufficient balance exists.
- `transfer(amount, other_category)`: Moves funds between categories if there are enough funds.
- `get_balance()`: Returns the current balance of the category.
- `check_funds(amount)`: Checks if there are enough funds for a withdrawal.
- `create_spend_chart(categories)`: Generates a bar chart for spending analysis.

## Example Usage
```python
food = Category('Food')
food.deposit(100, 'Grocery, Vegetables, Fish')
food.deposit(200, 'Coke, Chips, Biscuits')
food.withdraw(20, 'Taken money for tea')

clothing = Category('Clothing')
clothing.deposit(50, 'Jeans')
clothing.deposit(30, 'Shirt')
clothing.withdraw(50, 'Money for trouser')

food.transfer(70, clothing)

auto = Category('Auto')
auto.deposit(150, 'Fuel')
auto.deposit(530, 'Maintenance')
auto.withdraw(300, 'Car Repair')

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))
```

## Sample Output
```
**************Food**************
Grocery, Vegetables, Fi   100.00
Coke, Chips, Biscuits     200.00
Taken money for tea       -20.00
Transfer to Clothing      -70.00
Total: 210.00

************Clothing************
Jeans                      50.00
Shirt                      30.00
Money for trouser         -50.00
Transfer from Food         70.00
Total: 100.00

**************Auto**************
Fuel                      150.00
Maintenance               530.00
Car Repair               -300.00
Total: 380.00

Percentage spent by category
100|
 90|
 80|
 70|
 60|       o
 50|       o
 40|       o
 30|       o
 20| o     o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  t  t
     d  h  o
        i
        n
        g
```


