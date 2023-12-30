# This is the report of the solution
The process to build the $rational$ type is also described in the jupyter "test_notebook". 

After creating the basic structure of the rational class I needed to check whether the input precision was inside the required bound $[0,1]$. For this matter I used the $sys$ library to exit with an error in case this condition was not satisfied. 

I had to implement an algorithm to find the ratio and I went for the continued fraction first, just to have a solid algorithm to build the entire class; then after completing everything as optional I tested my naive algorithm. I tested the continued fraction algorithm on the jupyter notebook and when it was ready I wrote a module $cont_fract_mod.py$ in the "class_package" folder. The module was then called from the rational class to compute the ratio, paying attention to include possible negative numbers in the numerator.

Then I added all basic methods to the class: str, repr for representation; abs, add, sub, mul, truediv for arithmetics (I chose only to overload these operators because I think these are the only one for which $\mathbb{Q}$ is closed, but others can be implemented); gt, ge, lt, le, eq, ne for comparison; int, float as constructors. Then tested if these worked on the notebook
