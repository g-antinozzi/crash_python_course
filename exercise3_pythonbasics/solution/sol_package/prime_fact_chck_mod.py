from sol_package import prime_factors_mod as pfm

def prime_fact_chck():
    """This function checks for the correctness of the prime factorization of the numbers from 1 to 100
        
    Returns
    -------
    : boolean
      True if the re-factorized list has the same elements of the numbers from 1 to 100       
    """
     
    num_list = list(range(2, 101)) #one has no prime factorization (and is not prime)
    p_fact_list = [(1,)]
    
    for el in num_list:
        p_fact_list.append(pfm.prime_factorization(el)) #we use the prime_factorization module for each number from 2 to 100

    print("The prime factorization of numbers from 1 to 100: ", p_fact_list)

    refact_list = [] #list for the re-factorized integers
    
    for t in p_fact_list:
        tmp = 1
        for nums in t:
            tmp *= nums #we multiply again each factor
        refact_list.append(tmp) #build the re-factorized list

    check_list = list(range(1, 101)) #reference list for the check
    
    print("Is the check correct?")
    if refact_list == check_list:
        return True
    else:
        return False
    
