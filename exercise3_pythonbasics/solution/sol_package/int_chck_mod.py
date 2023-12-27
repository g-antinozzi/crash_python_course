import sys

def int_chck():
    """Asks for an integer and checks if it is an integer
        
    Returns
    -------
    a : int
        the integer to use
    """
    try: 
        a = int(input("Insert an integer: ")) #ask an integer to the user, the casting to int gives an error for strings and floats 
    except :
        sys.exit("What you inserted is not an integer!") #if not int we exit the program
    else:
        return a
