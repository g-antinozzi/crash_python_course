import math
from class_package.ex3_package import prime_factors_mod as pfm

def alt_rational(x, precision):
    """Given a real number x and a precision threshold we compute x as a fraction using a naive algorithm
       and we output the numerator and denominator of the fraction
       
    Parameters
    ----------
    x : float
        the real number to express as a fraction
    precision : float
        the precision threshold for the algorithm
 
    Returns
    -------
    : list
        the list with numerator and denominator
    """
    k=0 #truncation order

    n = math.floor(x) 
    d = 1

    while abs(n/d - x) > precision:
        n = int(round(x, k)*10**k) #naively we round the numerator to the highest order such that to reach the precision 
        d = 10**k #and take the denominator as the power of 10 to the truncation order
        k+=1

    #Ideally we could factorize any numerator (the prime_factorization function was implemented for the exercises3)
    t = list(pfm.prime_factorization(n)) 

    #The denominator is easy to factorize d = 2^k * 5^k
    Ntwos = 0
    Nfives = 0

     #Here we check how many twos and fives are in the prime factorization of n 
     #and take them out from the numerator since they are going to divide terms in the denominator
    for j in range(len(t)):
        if t[j] == 2:
            Ntwos+=1
            t[j] = 1
        elif t[j] == 5:
            Nfives+=1
            t[j] = 1


    n_fin = 1
    #Here we multiply all the remaining primes of the numerator factorization
    for vals in t: n_fin*=vals

    #We counted the twos and fives, so we know the factorization of the denominator
    d_fin = int(d/(2**Ntwos*5**Nfives))

    return list([n_fin, d_fin])