import matplotlib.pyplot as plt
from . import Expense

class BudgetList:
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        # Add items to expenses that are under budget
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item

    def __len__(self):
        return len(self.expenses) + len(self.overages)

    ##############
    ## Module 3 ##
    ##############

    # Goal is to create our own iterator for Budget class
    # To create iterator, follow the iterator protocol, that is have __iter__ and __next__
    def __iter__(self):
        # Since self.expenses and self.overages are lists, they each have built-in
        # iterators, so we will use their built-in iterators
        self.iter_e = iter(self.expenses) # returns an iterator
        self.iter_o = iter(self.overages) # returns an iterator
        return self

    def __next__(self):
        try:
            return self.iter_e.__next__()
        except StopIteration as stop:
            return self.iter_o.__next__()


def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    # read_expenses results in expenses.list to be populated
    expenses.read_expenses("data/spending_data.csv")
    for expense in expenses.list:
        myBudgetList.append(expense.amount)
    print("The count of all expenses: " + str(len(myBudgetList)))

    for entry in myBudgetList:
        print(entry)

    fig, ax = plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]

    ax.bar(labels, values, color=['green', 'red', 'blue'])
    ax.set_title('Your total expenses vs. total budget')

    plt.show()




if __name__ == "__main__":
    main()