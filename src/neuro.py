import math
import sys


def sigmoid(x: float):
    return 1.0 / (1.0 + math.exp(-x))


def learn(i1: float, i2: float, target_o1: float, target_o2: float):
    net_h1 = (learn.w1 * i1) + (learn.w2 * i2) + (b1 * 1)
    out_h1 = sigmoid(net_h1)
    
    print("learn ", i1, i2, "->", target_o1, target_o2)
   # print("out_h1", out_h1)
    
    net_h2 = (learn.w3 * i1) + (learn.w4 * i2) + (b1 * 1)
    out_h2 = sigmoid(net_h2)
    
   # print("out_h2", out_h2)
    
    
    net_o1 = (learn.w5 * out_h1) + (learn.w6 * out_h2) + (b2 * 1)
    out_o1 = sigmoid(net_o1)
    
    print("----------------")
    print("out_o1 %.2f" % out_o1)
    
    net_o2 = (learn.w7 * out_h1) + (learn.w8 * out_h2) + (b2 * 1)
    out_o2 = sigmoid(net_o2)
    
    print("out_o2 %.2f" % out_o2)
    print("----------------")
    
    Etotal = 1/2 * (target_o1 - out_o1)**2 + 1/2 * (target_o2 - out_o2)**2
    
    print("Etotal %.8f" % Etotal)
    
        
    ''' backpropagate '''
    
    delta_o1 = (out_o1 - target_o1) * out_o1 * (1 - out_o1)
    delta_o2 = (out_o2 - target_o2) * out_o2 * (1 - out_o2)
       
    dEtotal_dout_h1 = delta_o1 * learn.w5 + delta_o2 * learn.w7
    dEtotal_dout_h2 = delta_o1 * learn.w7 + delta_o2 * learn.w8
       
       
    dw1 = dEtotal_dout_h1 * out_h1 * (1 - out_h1) * i1
    dw2 = dEtotal_dout_h1 * out_h1 * (1 - out_h1) * i2
    dw3 = dEtotal_dout_h2 * out_h2 * (1 - out_h2) * i1
    dw4 = dEtotal_dout_h2 * out_h2 * (1 - out_h2) * i2
    
    dw5 = delta_o1 * out_h1
    dw6 = delta_o1 * out_h2
    dw7 = delta_o2 * out_h1
    dw8 = delta_o2 * out_h2
    
    
    learn.w1 = learn.w1 - n * dw1
    learn.w2 = learn.w2 - n * dw2
    learn.w3 = learn.w3 - n * dw3
    learn.w4 = learn.w4 - n * dw4    
    learn.w5 = learn.w5 - n * dw5
    learn.w6 = learn.w6 - n * dw6
    learn.w7 = learn.w7 - n * dw7
    learn.w8 = learn.w8 - n * dw8
     
        
    '''    
    print("dEtotal_dout_h1" , dEtotal_dout_h1)
    print("learn.w1+" , learn.w1)
    print("learn.w2+" , learn.w2)
    print("learn.w3+" , learn.w3)
    print("learn.w4+" , learn.w4)
    '''
   
    '''    
    print("learn.w5+", learn.w5)
    print("learn.w6+", learn.w6)
    print("learn.w7+", learn.w7)
    print("learn.w8+", learn.w8)
    '''
    
    print("\n")    

    

''' main '''

learn.w1 = .15
learn.w2 = .20 
learn.w3 = .25 
learn.w4 = .30 
learn.w5 = .40 
learn.w6 = .45
learn.w7 = .50
learn.w8 = .55

b1 = .35
b2 = .60

n = 10.0 # learning speed


for x in range(1, 1000):

    print(x)

    learn(0, 1, 0, 1)
    learn(1, 0, 1, 0)
    learn(1, 1, 1, 1)    
    learn(0, 0, 0, 0)
    #learn(.05, .10, .01, .99)






