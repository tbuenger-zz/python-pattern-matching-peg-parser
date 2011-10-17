from patternparser import *
    
def S(x):
    return expand(S,x)((
        (concat(S, S) ,                     lambda (s1,s2) : s1 + s2),
        (concat(sym('('), S, sym(')')),     lambda (l,s,r) : '<' + s + '>'),
        (concat(sym('('), sym(')')),        lambda x : '<>'),
        ))

print S('(()())()')