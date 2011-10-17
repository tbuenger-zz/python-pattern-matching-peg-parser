from patternparser import *

def Term(x):
    return expand(Term,x)((
        (concat(Brack, sym('+'), Brack) ,       lambda (l,o,r) : l + r ),
        (concat(Brack, sym('-'), Brack) ,       lambda (l,o,r) : l - r ),
        (concat(Brack, sym('*'), Brack) ,       lambda (l,o,r) : l * r ),
        (concat(Brack, sym('/'), Brack) ,       lambda (l,o,r) : l / r ),
        (Number,                                identity),
        ))   
        
def Brack(x):
    return expand(Brack,x)((
        (concat(sym('('), Term, sym(')')) ,     lambda (l,o,r) : o),
        (Number,                                identity),
        ))           

def Number(x):
    return expand(Number,x)((
        (concat(Number, Digit) ,                lambda (n, d) : (n * 10) + d),
        (Digit,                                 identity),
        ))   
   
def Digit(x):
    if x and x[0] in '0123456789':
        res = (ord(x[0])-ord('0'), x[1:])
        cacheit((Digit, x), res)
        return res
    return (None, x)   


def evaluate_and_print(expression):
    print expression + ' = ' + str(Term(expression))
    
evaluate_and_print('1300+37') 
  
evaluate_and_print('(2+3)*(1+4)')  