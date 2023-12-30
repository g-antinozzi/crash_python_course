import math

def cont_fract(x, precision):
    """Given a real number x and a precision threshold we compute x as a fraction using the continued fraction algorithm 
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

    #starting values
    n_list = list([1, math.floor(x)])
    d_list = list([0, 1])
    x_tmp = x - math.floor(x)

    #implementation of the algorithm
    while abs(n_list[1]/d_list[1] - x) > precision:
        a = math.floor(1/x_tmp)
        x_tmp = 1/x_tmp - a
        n_tmp = n_list[1]
        n_list[1] = a*n_list[1] + n_list[0]
        n_list[0] = n_tmp
        d_tmp = d_list[1]
        d_list[1] = a*d_list[1] + d_list[0]
        d_list[0] = d_tmp

    return list([n_list[1], d_list[1]])
