import expense_ops as ops

APP_BANNER = "=== Personal Expense Tracker v1.0 ==="


def main():
    while True:
        print(f"\n{APP_BANNER}")
        print("1. Add Expense")
        print("2. View All Expense")
        print("3. Delete Expense")
        print("4. Filter Expenses by Category")
        print("5. View Expense Summary")
        print("6. Search Expense by Keyword")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ").strip()

        if choice == "1" and hasattr(ops, "add_expense"):
            ops.add_expense()
        elif choice == "2" and hasattr(ops, "view_expenses"):
            ops.view_expenses()
        elif choice == "3" and hasattr(ops, "delete_expense"):
            ops.delete_expense()
        elif choice == "4" and hasattr(ops, "filter_by_category"):
            ops.filter_by_category()
        elif choice == "5" and hasattr(ops, "expense_summary"):
            ops.expense_summary()
        elif choice == "6" and hasattr(ops, "search_expenses"):
            ops.search_expenses()
        elif choice == "0":
            print("Exiting Personal Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice or feature not yet merged.")



if __name__ == "__main__":
    main()