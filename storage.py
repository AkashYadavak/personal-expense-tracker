import json
import os


DATA_FILE = "expenses.json"

# if file (expenses file) does not exsist then simple return the python list
# If exists then returns its data as the python list to work on.
# if exists but curropted then return the empty python list
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []



# take the expenses as a python list and write it in our DATA_FILE (expense file) in json format.
def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
