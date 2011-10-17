from patternparser import *

def RL(x):
    return expand(RL,x)((
        (concat(sym('a'), RL) ,   lambda (s1,s2) : 'b' + s2),
        (sym('a') ,              lambda a : 'b'),
        ))


def LL(x):
    return expand(LL,x)((
        (concat(LL, sym('a')) ,   lambda (s1,s2) : s1 + 'b'),
        (sym('a') ,              lambda a : 'b'),
        ))
    
            
    
print RL('aaaaaa')


print LL('aaaaaa')