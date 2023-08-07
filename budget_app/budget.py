class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance += entry["amount"]
    return balance

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
      return True
    return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    title = self.category.center(30, "*") + "\n"
    items = ""
    for entry in self.ledger:
      description = entry["description"][:23]
      amount = format(entry["amount"], ".2f").rjust(30 - len(description))
      items += f"{description}{amount}\n"
    total = f"Total: {format(self.get_balance(), '.2f')}"
    return title + items + total


def create_spend_chart(categories):
  spent = [(cat.category, sum(item["amount"] for item in cat.ledger if item["amount"] < 0)) for cat in categories]
  total_spent = sum(s for _, s in spent)
  spent_percentages = [(s / total_spent * 100) for _, s in spent]


  chart = "Percentage spent by category\n"
  for i in range(100, -1, -10):
    chart += str(i).rjust(3) + "| "
    for percentage in spent_percentages:
      chart += "o" if percentage >= i else " "
      chart += "  "
    chart += "\n"

  chart += "    -" + "---" * len(categories) + "\n"

  max_len = max([len(cat.category) for cat in categories])
  for i in range(max_len):
    chart += "     "
    for cat in categories:
      if i < len(cat.category):
        chart += cat.category[i] + "  "
      else:
        chart += "   "
    chart += "\n"

  return chart.rstrip("\n")
