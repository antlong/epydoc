# epydoc -- Backwards compatibility
#
# Copyright (C) 2005 Edward Loper
# Author: Edward Loper <edloper@loper.org>
# URL: <http://epydoc.sf.net>
#
# $Id: util.py 956 2006-03-10 01:30:51Z edloper $

"""
Backwards compatibility with previous versions of Python.

This module provides backwards compatibility by defining several
functions and classes that were not available in earlier versions of
Python.  Intented usage:

    >>> from epydoc.compat import *

Currently, epydoc requires Python 2.3+.
"""
__docformat__ = 'epytext'

######################################################################
#{ New in Python 2.4
######################################################################

# set
try:
    set
except NameError:
    try:
        from sets import Set as set, ImmutableSet as frozenset
    except ImportError:
        pass # use fallback, in the next section.

# sorted
try: 
    sorted
except NameError:
    def sorted(iterable, cmp=None, key=None, reverse=False):
        if key is None:
            elts = list(iterable)
        else:
            elts = [(key(v), v) for v in iterable]

        if reverse: elts.reverse() # stable sort.
        if cmp is None: elts.sort()
        else: elts.sort(cmp)
        if reverse: elts.reverse()
    
        if key is None:
            return elts
        else:
            return [v for (k,v) in elts]

# reversed
try: 
    reversed
except NameError:
    def reversed(iterable):
        elts = list(iterable)
        elts.reverse()
        return elts