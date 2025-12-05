class ExpenseTracker:
    def __init__(self) -> None:
        self.expenses: dict[str, int] = {}
        self.totalExpense = 0

    def add_expense(self, title: str, amount: int, category: str):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.totalExpense += amount

    def total_expense(self):
        return self.totalExpense

    def summary_by_category(self):
        return self.expenses

    def largest_expense(self):
        return max(self.expenses)



tracker = ExpenseTracker()
tracker.add_expense("Burger", 500, "food")
tracker.add_expense("Petrol", 2000, "travel")
tracker.add_expense("Burger", 500, "food")
tracker.add_expense("Petrol", 2000, "travel")
tracker.add_expense("Burger", 500, "food")
tracker.add_expense("Petrol", 2000, "travel")
tracker.add_expense("Burger", 500, "food")
tracker.add_expense("Petrol", 2000, "travel")
tracker.add_expense("Burger", 500, "food")
tracker.add_expense("Petrol", 2000, "travel")
print(tracker.expenses)
print(tracker.total_expense())
print(tracker.largest_expense())
