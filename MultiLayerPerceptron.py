#다중 퍼셉트론 구현 코드 

import numpy as np

def andPerceptron(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    netInput = x1*w1 + x2*w2
    if netInput <= theta:
        return 0
    elif netInput > theta:
        return 1

def nandPerceptron(x1,x2):
    w1,w2,theta = -0.5,-0.5,-0.7
    netInput = x1*w1 + x2*w2
    if netInput <= theta:
        return 0
    elif netInput > theta:
        return 1

def orPerceptron(x1,x2):
    w1,w2,bias = 0.5,0.5,-0.2
    netInput = x1*w1 + x2*w2 + bias
    if netInput <= 0:
        return 0
    elif netInput > 0:
        return 1

def xorPerceptron(x1,x2):
    s1 = nandPerceptron(x1,x2)
    s2 = orPerceptron(x1,x2)
    y = andPerceptron(s1,s2)
    return y

inputData = np.array([[0,0],[0,1],[1,0],[1,1]])

print("------and Perceptron ------")
for xs1 in inputData:
    print(str(xs1) + "==>" + str(andPerceptron(xs1[0],xs1[1])))
print("------nand Perceptron ------")
for xs2 in inputData:
    print(str(xs2) + "==>" + str(nandPerceptron(xs2[0],xs2[1])))
print("------or Perceptron ------")
for xs3 in inputData:
    print(str(xs3) + "==>" + str(orPerceptron(xs3[0],xs3[1])))
print("------XOR Perceptron ------")
for xs4 in inputData:
    print(str(xs4) + "==>" + str(xorPerceptron(xs4[0],xs4[1])))
