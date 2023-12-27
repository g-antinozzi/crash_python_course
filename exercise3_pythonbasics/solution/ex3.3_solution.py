# File: ex3.3_solution.py

from sol_package import div_chck_mod as dcm
from sol_package import int_chck_mod as icm
import time

if __name__ == '__main__':
    
    print("Find prime numbers up to which integer? ")
    N = icm.int_chck() 
    full_list = list(range(2, N+1)) #initial list

    k = 0
    #C1 = 0 #counter for speeding up the code
    
    tmp_len = len(full_list)
    #my implementation of the Sieve of Eratosthenes

    #st = time.time() #start time (used for the speed up)

    while k<tmp_len: #we loop up to the current number of numbers in the list
        j = k+1 #we start from checking from the next number on

        #C0 = tmp_len

        while j<tmp_len: #we check up to the current length of the list
            if dcm.div_checker(full_list[j], full_list[k]): #we check if the numbers bigger than k divide k, i.e. if they are a multiple of k.
                del full_list[j] #if they are, we remove them from the list
                tmp_len = len(full_list) #and update the length of the list
            j+=1

        #if C0 == tmp_len: #my euristic way to speed up the computation (did not look into the slowness):
                           #if the length of the array stays constant for more than two cycles we have the final list
        #    C1 += 1
        #if C1 > 2:
        #    break

        k+=1
        
    #et = time.time() #end time
    #print(et-st) #elapsed time in seconds

    #now full_list contains only prime numbers 
    print(f"List of prime numbers from 2 to {N}: ")
    print(full_list)
        
    
