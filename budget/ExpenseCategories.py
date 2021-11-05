import timeit

import matplotlib.pyplot as plt

from . import Expense


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()

    ##############################################
    ## Categorizing expenses into separate sets ##
    ##############################################
    divided_set_comp = expenses.categorize_set_comprehension()

    # Check if the sets output from each method are still the same
    if divided_set_comp != divided_for_loop:
        print('Sets are NOT equal by == test')

    # Another way to check if the sets output from each method are
    # still the same using zip() and subset()
    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print('Sets are NOT equal by subset test')

    # stmt="pass" --> This will eventually be the line of code we want to time the execution of.
    # setup = '''''' --> This multi-line string will eventually hold the lines of code that are required for stmt to run.
    # number = 1000 ---> This is the number of executions to time.
    # global = globals() --> This specifies the namespace to execute the code.

    print(timeit.timeit(
        stmt = "expenses.categorize_for_loop()",
        setup= '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
        ''',
        number=100000,
        globals=globals()
    ))

    print(timeit.timeit(
        stmt="expenses.categorize_set_comprehension()",
        setup='''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
        ''',
        number=100000,
        globals=globals()
    ))

    # You will see expenses.categorize_set_comprehension() takes
    # slightly longer than expenses.categorize_for_loop().
    # This is because cet comprehension may be faster than a for loop
    # in general for a single loop. However, we had 2 set comprehensions
    # that each required looping to check separate conditionals whereas
    # the for loop method only used one iteration to check the conditionals.

    fig, ax = plt.subplots()
    labels = ['Necessary', 'Food', 'Unnecessary']

    divided_expenses_sum = []
    for category_exps in divided_set_comp:
        divided_expenses_sum.append(
            sum(x.amount for x in category_exps)
        )

    ax.pie(divided_expenses_sum, labels=labels, autopct='%1.1f%%')
    plt.show()

if __name__ == "__main__":
    main()