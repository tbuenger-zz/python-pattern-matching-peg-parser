cache = {}
blacklist = set()

def concat(*args):
    def _concats(x):
        r = x
        result = ()
        for f in args:
            c = getfromcache(f, r)
            if c == resolving:
                return (None, x)
            (p,r) = c    
            if p is None:
                return (None, x)
            result += (p,)
        return (result, r) 
    return _concats
        
def sym(c):
    def _symbol(x):
        if x and x[0] == c:
            cacheit((sym, c, x), (c, x[1:]))
            return (c, x[1:])
        return (None, x)
    return _symbol

def cacheit(k,v):
    if (k,v) in blacklist:
        return False
    blacklist.add((k,v))
    cache[k] = v
    return True

def resolving():
    pass

def cachedordefault(f, x, default):
    if (f,x) in cache and not cache[(f,x)] == resolving:
        return cache[(f,x)]
    else:
        return default
    
def getfromcache(f, x):
    if (f,x) in cache:
        return cache[(f,x)]
    else:
        cache[(f,x)] = resolving
        return f(x)

def rules(f, x, args):
    def cacheandcall(v):
        if cacheit((f,x), v):
            return f(x)
        else:
            return cache[(f,x)]    
    
    def match(pattern, semantics):
        (p,r) = pattern(x)
        if p is not None:
            return cacheandcall((semantics(p), r))
        else:
            return None
        
    for (pattern, semantics) in args:
        result = match(pattern, semantics)
        if result is not None:
            return result
    
    return cachedordefault(f,x,(None, x))

def expand(f,x):
    return lambda args : rules(f,x,args)

def identity(x):
    return x