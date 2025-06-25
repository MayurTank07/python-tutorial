# expense_tracker.py

expenses = []

def add_expense(description, amount):
    """Adds a new expense to the list."""
    expenses.append({'description': description, 'amount': amount})

def get_total_expense():
    """Returns the total of all expenses."""
    return sum(item['amount'] for item in expenses)

def display_expenses():
    """Displays all added expenses."""
    for item in expenses:
        print(f"{item['description']} - ₹{item['amount']}")
