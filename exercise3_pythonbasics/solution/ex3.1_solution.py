# File: ex3.1_solution.py

def div_checker(a, b) :
    """Checks if a is divisible by b
    
    Parameters
    ----------
    a, b : int
           two numbers
        
    Returns
    -------
    : boolean
    """
    return a%b == 0

if __name__ == '__main__' :
    print("This script asks first for an integer and checks if it is divisible by 2,3,5 or 7.\nThen it asks for two integers and it checks if they are divisible by each other in any way.\n")
    try: 
        a = int(input("Insert an integer: "))
    except :
        print("What you inserted is not an integer.")
    else:
        s = 0
        for n in (2, 3, 5, 7):
            if div_checker(a, n):
                print(f"Your number is divisible by {n}")
            else:
                s+=1
        if s == 4:
            print("Your number is not divisible by 2,3,5 or 7")
    try: 
        b = int(input("\nInsert two integers\nfirst integer: "))
        c = int(input("second integer: "))
    except :
        print("What you inserted is not an integer.")
    else:
        if div_checker(b, c):
            if b != c:
                print(f"{b} is divisible by {c}")
                print(f"but {c} is not divisible by {b}") 
            else:
                print(f"{b} is surely divisible by {c}")
        elif div_checker(c, b):
            print(f"{b} is not divisible by {c}")
            print(f"but {c} is divisible by {b}")
        else:
            print("Your numbers are not divisible")
