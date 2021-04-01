
from itertools import combinations
from itertools import product
from fractions import Fraction
from math import factorial

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
    if n == 0 or k == 0:
        return 1
    elif k > n:
        return 0
    else:
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


# Subtracts two lists as vectors
def subtract(v, w):
    s = []
    for i in range(len(v)):
        s.append(v[i] - w[i])
    return s

# Returns True if the list contains an element greater than g, returns False otherwise
def greater_than_g(l, g):
    for i in l:
        if i > g:
            return True
    return False

# Returns True if list has one non-zero entry (i.e linear integrals), returns False otherwise
def linear(l):
    z = []
    nz = []
    for i in l:
        if i == 0:
            z.append(i)
        else:
            nz.append(i)
    if len(nz) == 1:
        return True, nz[0]
    else:
        return False, len(nz)


# Returns the various terms in the recursions
def Term(index, pure, twisted, i, g):
    i.sort()
    s = 0
    if (index == 1) and (pure == False) and (twisted == True):
        for g_2 in range(g):
            for l in Lists_Less_Than_Or_Equal_To(i):
                s += 2*((-1)**sum(l))*(binomial(2*g - 1, 2*g_2 + 1))*(Untwisted(subtract(i, l), g - 1 - g_2))*(Untwisted(l, g_2))
        return Fraction(s)
    if (index == 2) and (pure == False) and (twisted == True):
        for g_2 in range(1, g):
            for l in Lists_Less_Than_Or_Equal_To(i):
                s += 2*((-1)**sum(l))*(binomial(2*g - 1, 2*g_2))*(Twisted(subtract(i, l), g - g_2))*(Twisted(l, g_2))
        return Fraction(s)
    if (index == 1) and (pure == False) and (twisted == False):
        for g_2 in range(g):
            for l in Lists_Less_Than_Or_Equal_To(i):
                s += 2*((-1)**sum(l))*(binomial(2*g, 2*g_2 + 1))*(Twisted(subtract(i, l), g - g_2))*(Twisted(l, g_2))
        return Fraction(s)
    if (index == 2) and (pure == False) and (twisted == False):
        for g_2 in range(g):
            for l in Lists_Less_Than_Or_Equal_To(i):
                s += 2*((-1)**sum(l))*(binomial(2*g, 2*g_2 + 2))*(Untwisted(subtract(i, l), g - 1 - g_2))*(Untwisted(l, g_2))
        return Fraction(s)
    if (index == 1) and (pure == True) and (twisted == True):
        for r in range(1, i[-1] + 1):
            s += ((-1)**(i[-1] + 1))*(binomial(g - i[-1] + r, r + 1) + (1/2)*binomial(g - i[-1] + r, r))*(Twisted(i[:-1] + [i[-1] - r], g))
        return Fraction(s)
    if (index == 2) and (pure == True) and (twisted == True):
        for r in range(1, i[-1] + 1):
            s += (2*g + 1)*((-1)**i[-1])*(binomial(g - i[-1] + r, r + 1))*(Untwisted(i[:-1] + [i[-1] - r], g - 1))
        return Fraction(s)
    if (index == 3) and (pure == True) and (twisted == True):
        for g_2 in range(1, g):
            for l_2 in Lists_Less_Than_Or_Equal_To(i[:-1]):
                for p in range(i[-1] + 2):
                    for r in range(p + 1):
                        s += (2)*((-1)**(i[-1] + 2*g_2 - 1 - (i[-1] + 1 - p) - sum(l_2)))*(binomial(2*g + 1, 2*g_2))*(binomial(g - g_2 - p + r, r))*(Twisted(subtract(i[:-1], l_2) + [p - r], g - g_2))*(Twisted(l_2 + [i[-1] + 1 - p], g_2))
        return Fraction(s)
    if (index == 4) and (pure == True) and (twisted == True):
        for g_2 in range(1, g):
            for l_2 in Lists_Less_Than_Or_Equal_To(i[:-1]):
                for p in range(i[-1] + 1):
                    for r in range(p + 1):
                        s += ((-1)**(i[-1] + 2*g_2 - 1 - (i[-1] - p) - sum(l_2)))*(binomial(2*g + 1, 2*g_2))*(binomial(g - g_2 - p + r, r))*(Twisted(subtract(i[:-1], l_2) + [p - r], g - g_2))*(Twisted(l_2 + [i[-1] - p], g_2))
        return Fraction(s)
    if (index == 5) and (pure == True) and (twisted == True):
        for g_2 in range(1, g - 1):
            for l_2 in Lists_Less_Than_Or_Equal_To(i[:-1]):
                for p in range(i[-1] + 2):
                    for r in range(p + 1):
                        s += (2)*((-1)**(i[-1] + 2*g_2 - (i[-1] + 1 - p) - sum(l_2)))*(binomial(2*g + 1, 2*g_2 + 1))*(binomial(g - 1 - g_2 - p + r, r))*(Untwisted(subtract(i[:-1], l_2) + [p - r], g - 1 - g_2))*(Untwisted(l_2 + [i[-1] + 1 - p], g_2))
        return Fraction(s)
    if (index == 6) and (pure == True) and (twisted == True):
        for g_2 in range(1, g - 1):
            for l_2 in Lists_Less_Than_Or_Equal_To(i[:-1]):
                for p in range(i[-1] + 1):
                    for r in range(p + 1):
                        (2)*((-1)**(i[-1] + 2*g_2 - (i[-1] - p) - sum(l_2)))*(binomial(2*g + 1, 2*g_2 + 1))*(binomial(g - 1 - g_2 - p + r, r))*(Untwisted(subtract(i[:-1], l_2) + [p - r], g - 1 - g_2))*(Untwisted(l_2 + [i[-1] - p], g_2))
        return Fraction(s)


# Returns the hyperelliptic Hodge integral with all twisted points
def Twisted(i, g):
    i.sort()
    if (sum(i) > 2*g - 1) and g >= 1: #Zero for dimension reason
        return 0
    elif (sum(i) == 0) and g >= 0:  #Only psi classes
        return Fraction(1/2)
    elif greater_than_g(i, g) == True: #lambda_i = 0 for i > g
        return 0
    elif linear(i)[0] == True:
        return ((Fraction(1/2))**(linear(i)[1] + 1))*(Elementary_Symmetric_Function_Odd(linear(i)[1], g)) #linear integrals
    elif (sum(i) < 2*g - 1) and (g > 1):
        return Term(index=1, pure=False, twisted=True, i=i, g=g) - Term(index=2, pure=False, twisted=True, i=i, g=g)
    elif (sum(i) == 2*g - 1) and (g > 1):
        pure_hodge = 0
        for indices in [1, 2, 3, 4, 5, 6]:
            pure_hodge += Term(index=indices, pure=True, twisted=True, i=i, g=g)
        return Fraction(1/(i[-1]*((-1)**(i[-1] + 1))))*Fraction(pure_hodge)
    else:
        pass

# Returns the hyperelliptic Hodge integral with one untwisted point
def Untwisted(i, g):
    i.sort()
    if (sum(i) > 2*g) and g >= 1:  #Zero for dimension reason
        return 0
    elif (sum(i) == 0) and g >= 0:  #Only psi classes
        return Fraction(1/2)
    elif greater_than_g(i, g) == True: #lambda_i = 0 for i > g
        return 0
    elif linear(i)[0] == True:
        return ((Fraction(1/2))**(linear(i)[1] + 1))*(Elementary_Symmetric_Function_Even(linear(i)[1], g)) #linear integrals
    elif (sum(i) < 2*g) and g > 1:
        return Term(index=1, pure=False, twisted=False, i=i, g=g) - Term(index=2, pure=False, twisted=False, i=i, g=g)
    elif sum(i) == 2*g:  #pure hodge on the untwisted space is zero
        return 0
    else:
        pass























