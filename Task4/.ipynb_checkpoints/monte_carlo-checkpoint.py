import numpy as np 

expr = input("Enter function in terms of x: ")  #ask user for integral input
func = lambda x: eval(expr)  #change the input integral to a function so the method recognizes x as variable 
a = float(input("Lower bound:"))  #change the input to floats so they can be used in calculations 
b = float(input("Upper bound:"))

def monte_carlo(func, a, b):   #define function monte carlo, input function, lower bound, and upper bound 
    X = np.random.uniform(a, b, 1000)   #create an array between lower and upper bound, 1000 values 
    Y = np.array([func(i) for i in X])   #y-value at each of the 1000 values    
    return (b-a) * np.mean(Y)  #upper minus lower bound * the average y-value
    
monte_carlo(func, 0, 1)