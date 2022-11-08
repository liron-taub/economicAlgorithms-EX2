from typing import List
class Agent:
    def __init__(self, options):
        self.options = options

    def value(self, option:int)->float:
        return self.options[option]

def isParetoImprovement(agents:List[Agent], option1:int, option2:int)->bool:
    # will go all over the list and look for an improvement -
    # value thet is equal or greater then it.
    # here i will only chack greader because i will only send to the function numbers thet are diffrent
    # because the equal part is Easy to find
    for i in agents:
        # ensure thet the value of the other option is greater
        if i.value(option1) < i.value(option2):
            return False
    return True

def isParetoOptimal(agents:List[Agent], option:int, allOptions:List[int])->bool:
    # i will send to the isParetoImprovement function that checks whether ther is an improvement
    # if the return value is True it meens thet there is no improvement
    for optionAgents in allOptions:
        # if it equal we will just move on..
        if optionAgents == option:
            continue
        elif isParetoImprovement(agents, optionAgents, option):
            return False

    return True
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TEST: like what was givin to us in the matala:
agents = [Agent([1, 2, 3, 4, 5]),
          Agent([3, 1, 2, 5, 4]),
          Agent([3, 5, 5, 1, 1])]
allOptions = range(5)
def TEST1(agents, option1, option2):
    if isParetoImprovement(agents, option1, option2):
        print("Option " + str(option1) + " is pareto-improvement over " + str(option2) + "|")

def TEST2(agents, option, allOptions):
    if isParetoOptimal(agents, option, allOptions):
        print("option " + str(option) + " is pareto-optimal" + "           |")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("TEST1 : pareto improvement")
for opt1 in range(len(allOptions)):
    for opt2 in range(len(allOptions)):
        if opt1 == opt2:
            continue
        TEST1(agents, opt1, opt2)
print("__________________________")
print("TEST2 : pareto optimal:")
for opt in range(len(allOptions)):
    TEST2(agents, opt, allOptions)