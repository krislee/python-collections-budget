from . import Expense
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    main()