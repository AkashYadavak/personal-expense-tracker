from storage import load_expenses, save_expenses
from datetime import datetime


def add_expense():
    try:
        amount = float(input("Enter amount (INR): "))
        category = input("Enter category (Food/Travel/Bills/Shopping/Other): ").strip().title()
        description = input("Enter description: ").strip()
        date_str = datetime.now().strftime("%Y-%m-%d")

        expenses = load_expenses()
        new_id = max([e["id"] for e in expenses], default=0) + 1
        expenses.append({
            "id": new_id,
            "amount": amount,
            "category": category,
            "description": description,
            "date": date_str
        })
        save_expenses(expenses)
        print(f"Expenses added successfully (ID: {new_id}).")
    except ValueError:
        print("Invalid amount! Please enter a numeric value.")


def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"\n{'ID':<5} {'Date':<12} {'Category:<12'} {'Amount':<10} {'Description'}")
    print('-' * 60)
    for e in expenses:
        print(f"{e['id']:<5} {e['date']:<12} {e['category']:<12} {e['amount']:<10.2f} {e['description']}")


def delete_expense():
    view_expenses()
    expenses = load_expenses()
    if not expenses:
        return
    try:
        target_id = int(input("Enter Expense ID to delete: "))
        updated = [e for e in expenses if e["id"] != target_id]
        if len(updated) == len(expenses):
            print("Expense ID not found.")
        else:
            save_expenses(updated)
            print(f"Expense ID {target_id} deleted.")
    except ValueError:
        print("Please enter a valid numeric ID.")





def filter_by_category():
    category = input("Enter category to filter by: ").strip().title()
    expenses = [e for e in load_expenses() if e["category"] == category]
    if not expenses:
        print(f"No expenses found under '{category}'.")
        return
    print(f"\nExpenses in {category}:")
    for e in expenses:
        print(f"[{e['id']}] {e['date']} - {e['description']}: INR {e['amount']:.2f}")

def expense_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to summarize.")
        return
    total = sum(e["amount"] for e in expenses)
    breakdown = {}
    for e in expenses:
        breakdown[e["category"]] = breakdown.get(e["category"], 0) + e["amount"]

    print(f"\nTotal Spending: INR {total:.2f}")
    print("Category Breakdown:")
    for cat, amt in breakdown.items():
        pct = (amt / total) * 100
        print(f"  - {cat}: INR {amt:.2f} ({pct:.1f}%)")

def search_expenses():
    keyword = input("Enter keyword to search in descriptions: ").strip().lower()
    matches = [e for e in load_expenses() if keyword in e["description"].lower()]
    if not matches:
        print(f"No expenses matching '{keyword}'.")
        return
    print(f"\nSearch Results for '{keyword}':")
    for e in matches:
        print(f"[{e['id']}] {e['date']} | {e['category']} | {e['description']} | INR {e['amount']:.2f}")