
def addition(a,b):
    '''
    This is addition between for 2 digit
    module
        
    '''
    return a+b
    
def substraction(a,b):
        '''
        This is substraction for 
        2 digit module
        
        '''
        return a-b

def multiplication(a,b):
        '''
        
        This is multiplication for 
        2 digit module
        
        '''
        return a*b
    
def division(a,b):
        '''
        This is division into the 
        2 modules
        
        '''
        return a/b
    
def factorial(n):
        
        '''
        This is fact type 
        module
        '''
        if n >1:
            return "Can't find factorial on this nt"
        else:
            n = 1
            for i in range(n,0,-1):
                fact = fact*1
                
            return fact
        
def percenatage(obtain,total):
        '''
        This is percentage finder
        module intto overalll
        '''
        if obtain >total:
            obtain,total = total,obtain
            return obtain/total*100
        
        
        
        
