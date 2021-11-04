import collections
import matplotlib.pyplot as plt
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

spending_categories = []
for expense in expenses.list: # expenses.list is a list of Expense objects that was made in read_expenses
    spending_categories.append(expense.category)

# Count the number of categories using Counter() from collections
spending_counter = collections.Counter(spending_categories)
print(f'{spending_counter=}')

top5 = collections.Counter.most_common(spending_counter, 5)
print(f'{top5=}')

categories, count = zip(*top5)
print(f'{categories=} {count=}')

# fig = Figure aka top level container for the graph
# ax = Axes
fig, ax = plt.subplots()

ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()