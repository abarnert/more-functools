more-functools
==============

This module extends the standard-library's [functools](http://docs.python.org/library/functools.html), in much the same way that [more-itertools](http://pypi.python.org/pypi/more-itertools) extends [itertools](http://docs.python.org/library/itertools.html).

Most of the functions should be familiar from Haskell, Lisp, or other functional languages.

Replacement for functional
--------------------------
Collin Winter's [functional](http://web.archive.org/web/20101115214727/http://oakwinter.com/code/functional/documentation/index.html) module appears to be defunct; it doesn't quite work with 2.7, or at all with 3.x, without passing it through 2to3. However, it's still referenced in [the Python howto documentation](http://docs.python.org/release/2/howto/functional.html#the-functional-module) as of 2.7. The documentation for the module can be accessed via [the Wayback Machine](http://web.archive.org/web/20101115214727/http://oakwinter.com/code/functional/documentation/index.html).

The partial function is now in the standard library as functools.partial. The map and filter functions are unnecessary—the odd quirks with subclasses of standard sequence types are long gone; if you need to get a list you can always compose(list, map); if you don't like the behavior with None just don't pass it.  The id function has been renamed to identity, to avoid collision with the built-in.

But everything else has been reimplemented here. So, you can follow that howto and just change the name of the module you get the functions from.

Haskell Prelude functions
-------------------------
Python now has almost everything from the [Haskell Prelude](http://zvon.org/comp/r/ref-Haskell.html#Functions~Prelude) that makes sense for Python, but not quite everything.

Some of the missing functions are more iterator-related than HOF-related, so they can be found in more-itertools.

Other stuff
-----------
There are a few functions that are handy to have, even if they don't have an
impressive pedigree, so they're here.

Functions
=========

    compose(*funcs, unpack=False)

`compose(outer, middle, inner)` is equivalent to 
`outer(middle(inner(*args, **kw)))`.

`compose(outer, middle, inner, unpack=True)` is equivalent to `outer(*inner(*middle(*args, **kw)))`.

`compose(f)` is just `f`, and `compose()` is `identity`.
    
    const(x, *args, **kw)

Returns x, ignoring all other arguments.

    constantly(x)

Returns the function `const(x)`.

    flip(func)
    
Returns a function that's the equivalent of `func(*reversed(args), **kw)`.
    
    foldl(func, start, iterable)
    
`foldl(f, 0, [1, 2, 3])` is equivalent to `f(f(f(0, 1), 2), 3)`.
    
    foldl1(func, iterable)

`foldl1(f, iterable)` is equivalent to `foldl(f, next(iterable), iterable)`.

`foldl(f, [0, 1, 2, 3])` is equivalent to `f(f(f(0, 1), 2), 3)`.

    foldr(func, start, iterable)
    
`foldr(f, 0, [1, 2, 3])` is equivalent to `f(1, f(2, f(3, 0)))`.
    
    foldr1(func, iterable)

`foldr1(f, [1, 2, 3, 0])` is equivalent to `f(1, f(2, f(3, 0)))`.

    identity(x)

Returns x.

    nullable(func)

`nullable(f)` is equivalent to `None if any(arg is None for arg in args) else f(*args, **kw)`.
For example, `nullable(int)(None)` returns `None` instead of raising a `TypeError`.

    scanl(func, start, iterable)

`scanl(f, 0, [1, 2])` yields `0`, `f(0, 1)`, `f(f(0, 1), 2)`.

    scanl1(func, iterable)

`scanl1(f, [0, 1, 2])` yields `0`, `f(0, 1)`, `f(f(0, 1), 2)`. This is
identical to `itertools.accumulate(iterable, func)`.

    scanr(func, start, iterable)

`scanr(f, 0, [1, 2])` yields `f(1, f(2, 0))`, `f(2, 0)`, `0`.

    scanr1(func, iterable)

`scanr1(f, [1, 2, 0])` yields `f(1, f(2, 0))`, `f(2, 0)`, `0`.

