from sol_package import prime_mod as pm

def prime_factorization(n):
    """Given an integer this function outputs its prime factorization
        
    Parameters
    ----------
    n : int
        the integer to factorize
    Returns
    -------
    : tuple
        the tuple with the prime factors 
    """
    
    prime_tuple = tuple(pm.prime_list(n)) #tuple of prime numbers <= the given integer 
    factors = [] #list to append prime factors
    
    for p in prime_tuple: #we go through the prime number tuple
        if n%p == 0: #if n is divisible by the prime p, it's one of the factors
            factors.append(p) #we add it to the list
            tmp = n/p #here we account for the multiplicity of one of the primes 
            while tmp%p == 0: #we add to the list of factors until the tmp variable does not contain any more of the same prime
                factors.append(p)
                tmp /= p

    return tuple(factors)
