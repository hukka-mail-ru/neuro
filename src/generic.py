'''
Created on Jan 31, 2018

@author: hukka
'''




import show
import brain

 

if __name__ == '__main__': # pragma: no cover

    graphics = show.Graphics()
    
    b1 = .35
    b2 = 0.60            
    learningSpeed = 10.0 # learning speed
   

    minX = 99999999
    maxX = 0
    
    tries = 20
    
    av_min = 0
    av_max = 0
   
    for trie in range(1, tries):
   
   
        iNeurons = brain.createNeurons(brain.Neuron.Kind.I, 2) 
        hNeurons = brain.createNeurons(brain.Neuron.Kind.H, 4)
        oNeurons = brain.createNeurons(brain.Neuron.Kind.O, 2)  
                      
        neurons = iNeurons + hNeurons + oNeurons        
        
        brain.createSinapsesBetween(iNeurons, hNeurons)
        brain.createSinapsesBetween(hNeurons, oNeurons)
          
                  
        for x in range(1, 200):
        
            print("ONE", x)
            iNeurons[0].setValue(1)
            iNeurons[1].setValue(1)
            
            oNeurons[0].setTarget(0)
            oNeurons[1].setTarget(1)
                    
            err1 = brain.learn(hNeurons, oNeurons, learningSpeed)
            
            print("TWO", x)
            iNeurons[0].setValue(1)
            iNeurons[1].setValue(0)
            
            oNeurons[0].setTarget(1)
            oNeurons[1].setTarget(0)
                    
            err2 = brain.learn(hNeurons, oNeurons, learningSpeed)    
             
             
            if(err1 < 0.02 and err2 < 0.02):
                
                if(x < minX):
                    minX = x
                    av_min += x
    
                if(x > maxX):
                    maxX = x
                    av_max += x
                
                break 
             
        print("minX", minX)     
        print("maxX", maxX)     
                 
        ''' output ''' 
         
    
    
        for n in neurons:                
            n.draw(graphics)        
    
            for s in n.getOutSinapses():            
                s.draw(graphics)
                
    
        graphics.flip()    
        graphics.waitForKey()

