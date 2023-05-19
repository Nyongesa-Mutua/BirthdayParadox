import math

def bday_paradox():
    n = int(input("Enter the number of random people selected"))
    step_1 = math.factorial(n)
    step_2 = 365**n
    #combination part
    step_3_0 = math.factorial(365)
    step_3_1 = 365-n
    step_3_2 = math.factorial(step_3_1)
    step_3_3 = step_3_2*step_1
    comb = step_3_0/step_3_3
    p = step_1*comb/step_2
    prob = 1- p
    print(prob)

bday_paradox()