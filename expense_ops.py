from storage import load_expenses, save_expenses

def filter_by_category():
    category = input("Enter category to filter by: ").strip().title()
    expenses = [e for e in load_expenses() if e["category"] == category]
    if not expenses:
        print(f"No expenses found under '{category}'.")
        return
    print(f"\nExpenses in {category}:")
    for e in expenses:
        print(f"[{e['id']}] {e['date']} - {e['description']}: INR {e['amount']:.2f}")
        