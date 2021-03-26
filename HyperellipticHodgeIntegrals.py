
from itertools import combinations
from fractions import Fraction

def product_of_tuple(t):
    p = 1
    for i in t:
        p *= i
    return p

#Returns a list of the first g odd numbers
def first_g_odd(g):
    return [2*i - 1 for i in range(1, g + 1)]

#Returns the ith elementary symmetric function on the first g odd numbers
def Elementary_Symmetric_Function_Odd(i, g):
    s = 0
    for i_tuple in combinations(first_g_odd(g), i):
        s += product_of_tuple(i_tuple)
    return s

#Returns a list of the first g even numbers
def first_g_even(g):
    return [2*i for i in range(1, g + 1)]

#Returns the ith elementary symmetric function on the first g even numbers
def Elementary_Symmetric_Function_Even(i, g):
    s = 0
    for i_tuple in combinations(first_g_even(g), i):
        s += product_of_tuple(i_tuple)
    return s








