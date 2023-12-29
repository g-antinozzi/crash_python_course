# File: ex3.4_solution.py

from sol_package import prime_factors_mod as pfm
from sol_package import int_chck_mod as icm
from sol_package import prime_fact_chck_mod as pfcm

if __name__ == '__main__' :
    
    print("In this program we first find the prime factorization of a given integer, then we check the correctness of the prime factorization for all numbers from 1 to 100.\n")
    n = icm.int_chck()
    print("The prime factors are: ", pfm.prime_factorization(n), "\n")

    if pfcm.prime_fact_chck():
        print("yes")
    else:
        print("no")
    
