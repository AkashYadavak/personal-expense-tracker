# Personal Expense Tracker (Console Edition)

A lightweight, **command-line personal finance application** built in Python that allows users to record, inspect, filter, search, and summarize daily expenses with persistent JSON storage.

## Project Objectives
- Practice collaborative software development using **Git** and **GitHub**.
- Implement modular Python code separated across multiple source files.
- Demonstrate branching, pull requests, peer code reviews, and merge conflict resolution.

## Team Members & Contributions
| Student Role | Name | Roll Number | Branch | Key Contributions |
| :--- | :--- | :--- | :--- | :--- |
| **Student 1** | `Akash Yadav` | `08` | `Akash-branch` | Repo setup, `storage.py`, Add/View/Delete expenses, `README.md` |
| **Student 2** | `Waquas Ahmed` | `67` | `Waquas-branch` | Filter by category, Spending summary, Keyword search, Conflict resolution, `CONTRIBUTING.md` |

## Features & Technologies
- **Add Expense:** Record amount, category, description, and automatic date stamp.
- **View All Expenses:** Tabular console display of all saved records.
- **Delete Expense:** Remove entries safely by record ID.
- **Filter & Search:** Filter by category or search descriptions by keyword.
- **Expense Summary:** Calculates total spending and category-wise percentage breakdown.
- **Technologies:** [Python 3.x](https://www.python.org/), JSON Standard Library, [Git](https://git-scm.com/), and [GitHub](https://github.com/).

## Project Structure
```text
personal-expense-tracker/
├── main.py            # CLI menu and application entry point
├── expense_ops.py     # Core CRUD, filter, search, and summary operations
├── storage.py         # JSON file persistence layer
├── .gitignore         # Ignored cache and local data files
├── README.md          # Project documentation
└── CONTRIBUTING.md    # Collaboration and Git workflow details
```

## Installation & Execution

1. Clone the repository:

```bash
git clone [https://github.com/](https://github.com/)AkashYadavak/personal-expense-tracker.git
cd personal-expense-tracker
```

2. Run the application:

```bash
python main.py
```

## Sample Output

```bash
=== Personal Expense Tracker v1.0 (Pro Console Edition) ===
1. Add Expense
2. View All Expenses
3. Delete Expense
4. Filter Expenses by Category
5. View Expense Summary
6. Search Expenses by Keyword
0. Exit
Enter your choice (0-6): 5

Total Spending: INR 1450.00
Category Breakdown:
  - Food: INR 450.00 (31.0%)
  - Travel: INR 1000.00 (69.0%)
```


