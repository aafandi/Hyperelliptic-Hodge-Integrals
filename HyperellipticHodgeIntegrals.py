from itertools import combinations
from itertools import product
from fractions import Fraction
from math import factorial

#Returns the product of the numbers in a tuple t
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

#Returns n choose k
def binomial(n, k):
    return Fraction(factorial(n)/(factorial(k)*factorial(n-k)))


#Returns a list of all lists lexicographically less than or equal to the input list
def Lists_Less_Than_Or_Equal_To(l):

    returned_list = []
    X = [[i] for i in range(l[0] + 1)]

    if len(l) == 1:
        return X

    without_first_index = l
    without_first_index.pop(0)

    Y = Lists_Less_Than_Or_Equal_To(without_first_index)

    for i, j in product(X, Y):
        returned_list.append(i + j)

    return returned_list








