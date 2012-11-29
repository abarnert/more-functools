try:
        from setuptools import setup
except:
        from distutils.core import setup

dist = setup(
    name = 'more-functools',
    version = '0.1.0',
    description = "More tools for functional programming in python",
    
    long_description = """more-functools extends the standard library's
functools, in much the same way that more-itertools extends itertools. It
is also a replacement for the defunct functional module by Collin Winters.""",
        
    author = 'Andrew Barnert',
    author_email = 'abarnert@yahoo.com',
    url = 'http://github.com/abarnert/more-functools/',
    license = 'MIT',
    classifiers = [     
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords = 'python functional higher-order',    
    modules = ['more_functools'],
    test_suite = 'tests',
)
