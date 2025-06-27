# expense_tracker.py

expenses = []
# ("Tea", 15)
# ("Lunch", 120)
# ("Transport", 50)
# ("Transport", 100)
# ("Dinner", 3500)

def add_expense(description, amount):
    expenses.append({'description': description, 'amount': amount})

def get_total_expense():
    return sum(item["amount"] for item in expenses)

def display_expenses():
    for item in expenses:
        print(f"{item['description']} - ₹{item['amount']}")
