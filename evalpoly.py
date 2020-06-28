import cmath
def poly(p,z):
    '''arguments are: a polynomial given as a list of coefficients- constant, degree1, degree2,..all of which are complex nunmbers  and a point z at which we want to evaluate the polynomial.Returns the answer as a complex number'''
    if p==[]:
        return complex(0)
    n=len(p)
    v=complex(0)
    powers=[1]
    for i in range(n):
        if i>0:
            powers.append(powers[i-1]*z)
    for i in range(n):
        v+=p[i]*powers[i]
    return v
