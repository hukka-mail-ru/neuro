import math


def sigmoid(x: float):
    return 1.0 / (1.0 + math.exp(-x))

def error(expected: float, actual: float, tries: int):
    return (expected - actual)**2 /  tries

w1=0.45
w2=0.78 
w3=-0.12 
w4=0.13 
w5=1.5 
w6=-2.3

E = 0.7
A = 0.3


''' 1  '''
I1 = 1
I2 = 0
expectedO1 = 1


olddw1 = 0 
olddw2 = 0 
olddw3 = 0 
olddw4 = 0 

for x in range(1, 100):

    H1input = (I1 * w1) + (I2 * w3)
    H1 = sigmoid(H1input)
    
    H2input = (I1 * w2) + (I2 * w4)
    H2 = sigmoid(H2input)
    
    O1input = (H1 * w5) + (H2 * w6)
    O1 = sigmoid(O1input)
    
    print("O1", O1)
    
    e = error(expectedO1, O1, 1)
    
    print("e", e)
    
    
    ''' backpropagate '''
    
    deltaO1 = (expectedO1 - O1) * (1 - O1) * O1
    
    deltaH1 = (1 - H1) * H1 * (w5 * deltaO1)
    GRADw5 = H1 * deltaO1
    dw5 = E * GRADw5 + A * 0
    w5 += dw5
    
    
    deltaH2 = (1 - H2) * H2 * (w6 * deltaO1)
    GRADw6 = H2 * deltaO1
    dw6 = E * GRADw6 + A * 0
    w6 += dw6
    
    
    deltaI2 = (1 - I2) * I2 * (w1 * deltaH1 + w2 * deltaH2)
    
    GRADw1 = I1 * deltaH1
    dw1 = E * GRADw1 + A * 0
    olddw1 = dw1
    w1 += dw1
    
    GRADw2 = I1 * deltaH2
    dw2 = E * GRADw2 + A * 0
    olddw2 = dw2
    w2 += dw2
    
    GRADw3 = I2 * deltaH1
    dw3 = E * GRADw3 + A * 0
    olddw3 = dw3
    w3 += dw3
    
    GRADw4 = I2 * deltaH2
    dw4 = E * GRADw4 + A * 0
    olddw4 = dw4
    w4 += dw4





