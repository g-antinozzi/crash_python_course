import copy

def fibonacci(n):
    """A function that calculates the Fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    : list
        a list with the Fibonacci sequence
    """
    t = [0,1] #values starting the sequence
    for k in range(2,n+1):
        t.append(t[k-1]+t[k-2]) #append new fibonacci numbers
    return t

if __name__ == '__main__':
    print("Given the n-th index we show the list of Fibonacci numbers, then we divide the list into odd and even numbers.")
    
    try: 
        n = int(input("\nYou want to see Fibonacci numbers up to which index? ")) #ask the final index
    except :
        print("What you inserted is not an integer.") #check for errors
    else:
        a = fibonacci(n) #compute the numbers with the function defined
        print(f"The list of Fibonacci numbers up to index {n} is: ", a)
    
        a_odd = copy.deepcopy(a) #make a new object from which we pop even numbers, thus remaining with odds and we still have the original a
        a_even = []
    
        for idx, el in enumerate(a_odd):
            if el%2 == 0:
                a_even.append(a_odd.pop(idx))
        print("The sublist of even Fibonacci numbers is: ", a_even)
        print("The sublist of odd Fibonacci numbers is: ", a_odd)
