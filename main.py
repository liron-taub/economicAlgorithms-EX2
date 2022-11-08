# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Agent import Agent, TEST1,TEST2
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    agents = [Agent([1, 2, 3, 4, 5]), Agent([3, 1, 2, 5, 4]), Agent([3, 5, 5, 1, 1])]
    allOptions = range(5)
    print("pareto-improvement:")
    for option1 in range(len(allOptions)):
        for option2 in range(len(allOptions)):
            if option1 == option2:
                continue
            TEST1(agents, option1, option2)
    print("pareto-optimal:")
    for opt in range(len(allOptions)):
        TEST2(agents, opt, allOptions)