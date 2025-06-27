# main.py

import expense_tracker as et

# Add expenses
et.add_expense("Tea", 15)
et.add_expense("Lunch", 120)
et.add_expense("Transport", 50)
et.add_expense("Transport", 100)
et.add_expense("Dinner", 50)

# Display expenses
print("Your Expenses Today:")
et.display_expenses()

# Show total
print(f"\nTotal Spent: ₹{et.get_total_expense()}")
