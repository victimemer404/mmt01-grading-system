#10SUBJECTS

import random as rand
import statistics
import sys

arithmeticMeanFile = open("AM-10sub.txt", "a")

def x_x(f_weight, a_weight, GRADES, i):
    formative = GRADES[i][0]
    alternative = GRADES[i][1]

    return (abs(f_weight - formative) + abs(a_weight - alternative))/2

iterations = 1_000_000
while(iterations > 0):
    #SIZE = len(['Math', 'Eng', 'Bio', 'Chem', 'Phys'])
    SIZE = len(['IS', 'Math', 'Eng', 'SS', 'Fil', 'PEHM', 'VE', 'AdTech', 'CS', 'ES'])
    UNITS = [2, 1.7, 1.3, 1, 1, 1, 0.7, 1, 1, 0.7]
    GRADES = [(0.65, 0.25), (0.8, 0.2), (0.7, 0.2), (0.5, 0.5), (0.55,  0.45), (0.5, 0.5), (0.6, 0.4), (0.75, 0.25), (0.65, 0.25), (0.75, 0.25)]

    c_grade = [rand.randint(35, 45) for i in range(SIZE)]
    weightChangeList = []

    result = int(0)

    for i in range(SIZE):
        f_assessments = rand.randint(8, 16)
        a_assessments = rand.randint(1, 8)

        f_weight = (1 - c_grade[i]/100) * f_assessments / (f_assessments + a_assessments)
        a_weight = (1 - c_grade[i]/100) * a_assessments / (f_assessments + a_assessments)

        weightChangeList += [x_x(f_weight, a_weight, GRADES, i)]

    result = statistics.mean(weightChangeList)
    print(result, file=arithmeticMeanFile)
        
    iterations -= 1
