import sys
import math
from class_package import cont_fract_mod as cfm
from class_package import alt_rational_mod as arm

class rational () :
    """This class creates a new type called "rational". It has a positional argument "num" which is the number from which its rational version is obtained and two keyword arguments "precision", the precision with which the ratio approximates "num", default at 1e-5, and "algorithm", which is the choice of the algorithm to compute the ratio, either continued fraction algorithm ("cont_fract" as default) or a naive one ("naive_alg").
    """
    
    def __init__ (self, num, precision = 1.e-5, algorithm = "cont_fract"):
        if precision<0 or precision>1:
            sys.exit("The precision used is not between [0,1]")
            
        self.num = num
        self.precision = precision
        num_tmp = abs(self.num)
        if algorithm == "cont_fract":
            cont_fract_list = cfm.cont_fract(num_tmp, self.precision)
        
            self.denominator = cont_fract_list[1]
        
            if self.num < 0:
                self.numerator = -cont_fract_list[0]
            else:
                self.numerator = cont_fract_list[0]
        elif algorithm == "naive_alg":
            naive_alg_list = arm.alt_rational(num_tmp, self.precision)
        
            self.denominator = naive_alg_list[1]
        
            if self.num < 0:
                self.numerator = -naive_alg_list[0]
            else:
                self.numerator = naive_alg_list[0]
                
    #Representation operators
    
    def __str__ ( self ) :
        return f'{self.numerator}/{self.denominator}'
    
    def __repr__ ( self ) :
        return f'{type(self).__name__}({self.num}, precision={self.precision})'    
    
    #Arithmetic operators
    
    def __abs__ (self) :
        return type(self) (abs(self.numerator)/self.denominator)
    
    def __add__ (self, other) :
        return type(self) (self.numerator/self.denominator+other.numerator/other.denominator)
    
    def __sub__ (self, other) :
        return type(self) (self.numerator/self.denominator-other.numerator/other.denominator)
    
    def __mul__ (self, other) :
        return type(self) ((self.numerator/self.denominator)*(other.numerator/other.denominator)) 

    def __truediv__ (self, other) :
        return type(self) ((self.numerator/self.denominator)/(other.numerator/other.denominator))
    
    
    #Comparison operators
    
    def __eq__ (self, other) :
        return (self.numerator, self.denominator) == (other.numerator, other.denominator)
    
    def __ne__ (self, other) :
        return (self.numerator, self.denominator) != (other.numerator, other.denominator)
    
    def __gt__ (self, other) :
        return self.numerator * other.denominator > other.numerator * self.denominator
    
    def __ge__ (self, other) :
        return self.numerator * other.denominator >= other.numerator * self.denominator
    
    def __lt__ (self, other) :
        return self.numerator * other.denominator < other.numerator * self.denominator
    
    def __le__ (self, other) :
        return self.numerator * other.denominator <= other.numerator * self.denominator
    
    # overload of two constructors
    def __int__ (self) :
        return int(self.numerator/self.denominator)
    
    def __float__ (self) :
        return float(self.numerator/self.denominator)
