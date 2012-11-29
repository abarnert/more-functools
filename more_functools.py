from functools import partial, wraps

# reduce is a built-in in 2.x, in functools in 3.x
try:
    from functools import reduce
except ImportError:
    pass

# accumulate was added in 3.2
try:
    from itertools import accumulate
except ImportError:
    import operator
    def accumulate(iterable, func=operator.add):
        iterable = iter(iterable)
        total = next(iterable)
        yield total
        for element in iterable:
            total = func(total, element)
            yield total

__all__ = ['compose', 'const', 'constantly', 'flip',
           'foldl', 'foldl1', 'foldr', 'foldr1',
           'identity', 'nullable',
           'scanl', 'scanl1', 'scanr', 'scanr1']

# These first two really belong in more_itertools, but we need them here.
def append(value, iterable):
    for element in iterable:
        yield element
    yield value

def prepend(value, iterable):
    yield value
    for element in iterable:
        yield element

def flip(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f(*reversed(*args), **kwargs)
    return wrapper

def identity(x):
    return x
    
def compose(*funcs, **kwargs):
    unpack = kwargs.get('unpack', False)
    if not funcs: return identity
    outer, funcs = funcs[-1], reversed(funcs[:-1])
    if unpack:
        @wraps(outer)
        def wrapper(*args, **kwargs):
            ret = outer(*args, **kwargs)
            for func in funcs:
                ret = func(*ret)
            return ret
    else:
        @wraps(outer)
        def wrapper(*args, **kwargs):
            ret = outer(*args, **kwargs)
            for func in funcs:
                ret = func(ret)
            return ret
    return wrapper

def const(x, *args, **kwargs):
    return x

def constantly(x):
    @wraps(const)
    def wrapper(*args, **kwargs):
        return x
    return wrapper
        
def foldl(func, start, iterable):
    return reduce(func, iterable, start)

def foldl1(func, iterable):
    return reduce(func, iterable)

def _foldr(func, start, iterable):
    try:
        first = next(iterable)
    except StopIteration:
        return start
    return func(first, _foldr(func, start, iterable))
    
def foldr(func, start, iterable):
    return _foldr(func, start, iter(iterable))

def _foldr1(func, iterable):
    first = next(iterable)
    try:
        return func(first, _foldr1(func, iterable))
    except StopIteration:
        return first

def foldr1(func, iterable):
    try:
        return _foldr1(func, iter(iterable))
    except StopIteration:
        raise TypeError('foldr1() of empty sequence')

def scanl(func, start, iterable):
    return accumulate(prepend(start, iterable), func)

def scanl1(func, iterable):
    return accumulate(iterable, func)

def _scanr(func, start, iterable):
    try:
        first = next(iterable)
    except StopIteration:
        yield start
        raise StopIteration
    rest = _scanr(func, start, iterable)
    value = next(rest)
    yield func(first, value)
    yield value
    for value in rest:
        yield value
    
def scanr(func, start, iterable):
    return _scanr(func, start, iter(iterable))

def _scanr1(func, iterable):
    first = next(iterable)
    try:
        rest = _scanr1(func, iterable)
        value = next(rest)
        yield func(first, value)
        yield value
        for value in rest:
            yield value
    except StopIteration:
        yield first

def scanr1(func, iterable):
    return _scanr1(func, iter(iterable))

def nullable(func):
    # TODO: This really should require the mandatory arguments of
    # func, and not allow extra arguments if func doesn't. If you call
    # nullable(int)('3', 10, None), it should be a TypeError.
    @wraps(func)
    def wrapper(*args, **kwargs):
        if any(arg is None for arg in args): return None
        return func(*args, **kwargs)
    return wrapper
