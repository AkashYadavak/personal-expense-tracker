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