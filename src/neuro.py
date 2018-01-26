import math
import sys

def sigmoid(x: float):
    return 1.0 / (1.0 + math.exp(-x))

w1 = .15
w2 = .20 
w3 = .25 
w4 = .30 
w5 = .40 
w6 = .45
w7 = .50
w8 = .55

b1 = .35
b2 = .60

n = 10.0 # learning speed



''' 1  '''
i1 = .05
i2 = .10


target_o1 = .01
target_o2 = .99

'''
olddw1 = 0 
olddw2 = 0 
olddw3 = 0 
olddw4 = 0 
sumKv = 0
'''

for x in range(1, 100):

    net_h1 = (w1 * i1) + (w2 * i2) + (b1 * 1)
    out_h1 = sigmoid(net_h1)
    
    print("out_h1", out_h1)
    
    net_h2 = (w3 * i1) + (w4 * i2) + (b1 * 1)
    out_h2 = sigmoid(net_h2)
    
    print("out_h2", out_h2)
    
    
    net_o1 = (w5 * out_h1) + (w6 * out_h2) + (b2 * 1)
    out_o1 = sigmoid(net_o1)
    
    print("----------------")
    print("out_o1", out_o1)
    
    net_o2 = (w7 * out_h1) + (w8 * out_h2) + (b2 * 1)
    out_o2 = sigmoid(net_o2)
    
    print("out_o2", out_o2)
    print("----------------")
    
    Etotal = 1/2 * (target_o1 - out_o1)**2 + 1/2 * (target_o2 - out_o2)**2
    
    print("Etotal", Etotal)
    
        
    ''' backpropagate '''
    
    dw5 = (out_o1 - target_o1) * out_o1 * (1 - out_o1) * out_h1
    dw6 = (out_o1 - target_o1) * out_o1 * (1 - out_o1) * out_h2
    dw7 = (out_o2 - target_o2) * out_o2 * (1 - out_o2) * out_h1
    dw8 = (out_o2 - target_o2) * out_o2 * (1 - out_o2) * out_h2
   
    dEtotal_dout_h1 = (out_o1 - target_o1) * out_o1 * (1 - out_o1) * w5 + (out_o2 - target_o2) * out_o2 * (1 - out_o2) * w7
   
    dw1 = dEtotal_dout_h1 * out_h1 * (1 - out_h1) * i1
    dw2 = dEtotal_dout_h1 * out_h1 * (1 - out_h1) * i2
    
    w1 = w1 - n * dw1
    w2 = w2 - n * dw2
    
    
    
    dEtotal_dout_h2 = (out_o1 - target_o1) * out_o1 * (1 - out_o1) * w7 + (out_o2 - target_o2) * out_o2 * (1 - out_o2) * w8
   
    dw3 = dEtotal_dout_h2 * out_h2 * (1 - out_h2) * i1
    dw4 = dEtotal_dout_h2 * out_h2 * (1 - out_h2) * i2
    
    w3 = w3 - n * dw3
    w4 = w4 - n * dw4
   
    print("dEtotal_dout_h1" , dEtotal_dout_h1)
    print("w1+" , w1)
    print("w2+" , w2)
    print("w3+" , w3)
    print("w4+" , w4)
   
    w5 = w5 - n * dw5
    w6 = w6 - n * dw6
    w7 = w7 - n * dw7
    w8 = w8 - n * dw8
        
    print("w5+", w5)
    print("w6+", w6)
    print("w7+", w7)
    print("w8+", w8)

    
    print("\n")



