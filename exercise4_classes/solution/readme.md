# This is the report of the solution
The process to build the $rational$ type is also described in the jupyter "test_notebook". 

After creating the basic structure of the rational class I needed to check whether the input precision was inside the required bound $[0,1]$. For this matter I used the $sys$ library to exit with an error in case this condition was not satisfied. 

I had to implement an algorithm to find the ratio and I went for the continued fraction first, just to have a solid algorithm to build the entire class; then after completing everything as optional I tested my naive algorithm. I tested the continued fraction algorithm on the jupyter notebook and when it was ready I wrote a module $cont\textunderscore fract\textunderscore mod.py$ in the "class_package" folder. The module was then called from the rational class to compute the ratio, paying attention to include possible negative numbers in the numerator.

Then I added all basic methods to the class: str, repr for representation; abs, add, sub, mul, truediv for arithmetics (I chose only to overload these operators because I think these are the only one for which $\mathbb{Q}$ is closed, but others can be implemented); gt, ge, lt, le, eq, ne for comparison; int, float as constructors. Then tested if these worked on the notebook.

As optional I went back to the ratio algorithm and build my own using the prime factorization I implemented for ex3.4. What I did was: 
- Take the input number $x$ and get the first approximation for the ratio as $n = \lfloor x \rfloor$, $d = 1$ $\Rightarrow x = n/d$
- Then within a while loop with condition $|n/d - x| > precision$; for each loop I took $n$ as the rounded version with $k$ decimal digits of $x$ and $d = 10^k$, starting with $k=0$ and increasing by one for each loop. This is simply the naive algorithm if $x = a_0,a_1...a_m$, at order k of rounding truncation it will be $x_k = a_0a_1...\rm{r}(a_k)/10^k$ with $r(a_k)$ the roundend k-th digit. When $|x_k - x|< precision$ I exit the while loop.
- Then I found the prime factors of n and counted how many 2s and 5s it had, these are then taken away from $d$ since $d = 2^k 5^k$ and also from n.
- Remultiplying the remaining prime factors for n, I finally have the ratio.
It works good enough, but the bottleneck remains the prime factorization of n, which takes too long for numbers of $O(10^6)$ due to my own simple algorithm to factorize integers.

I left out the hashable part, but maybe I will try it in the future.
