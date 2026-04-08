import csv

def save_data(income_entries, expense_entries):
    with open("john123_income.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "amount", "source"])
        writer.writeheader()
        writer.writerows(income_entries)

    with open("john123_expense.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "amount", "category"])
        writer.writeheader()
        writer.writerows(expense_entries)


def load_data():
    income_entries = []
    expense_entries = []

    try:
        with open("john123_income.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                income_entries.append({
                    "date": row["date"],
                    "amount": float(row["amount"]),
                    "source": row["source"]
                })
    except:
        pass

    try:
        with open("john123_expense.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                expense_entries.append({
                    "date": row["date"],
                    "amount": float(row["amount"]),
                    "category": row["category"]
                })
    except:
        pass

    return income_entries, expense_entries