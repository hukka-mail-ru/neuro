'''
Created on Jan 31, 2018

@author: hukka
'''




import show
import brain

 

if __name__ == '__main__': # pragma: no cover

    graphics = show.Graphics() 
    brain = brain.Brain()
    
    b1 = .35
    b2 = 0.60            
    learningSpeed = 10.0 # learning speed
   

    minX = 99999999
    maxX = 0
    
    tries = 20
    
    av_min = 0
    av_max = 0
   
    for trie in range(1, tries):
   
        brain.clear()
        brain.create(2, 4, 2)
           
                   
        for x in range(1, 200):
        
            print("\nONE", x)            
            brain.teach([0,1], [0,1])       
            err1 = brain.learn(learningSpeed)
            
            
            print("TWO", x)                        
            brain.teach([1,0], [0,1])      
            err2 = brain.learn(learningSpeed)    
             
             
            print("THREE", x)                        
            brain.teach([1,1], [1,1])      
            err3 = brain.learn(learningSpeed)  
            
            print("FOUR", x)                        
            brain.teach([0,0], [0,0])      
            err4 = brain.learn(learningSpeed)  
             
            if(err1 < 0.02 and err2 < 0.02 and err3 < 0.02  and err4 < 0.02 ):
                
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
         
    
        brain.draw(graphics)
                
    
        graphics.flip()    
        graphics.waitForKey()
        graphics.clearScreen()

