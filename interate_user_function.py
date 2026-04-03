from numpy import sin, cos, exp, pi
from scipy.integrate import quad
import numpy as np

def f(x, f_str):
    try:
        return eval(f_str)  #return input formula 
    except NameError:
        print("unknown function or variable")  #unknown function 
    except Exception:
        print("invalid expression")  #wrong expression 

f_str = input("Enter f(x): ")
print(f(1.0, f_str))

def g(x):
    return x**4 + np.exp(np.sin(x) + np.cos(x))  #given expression 

print(quad(g, 0, np.pi))  #integrate using scipy.integrate.quad

x = np.random.uniform(0, np.pi, 10000)  #create random distribtion for monte carlo integration 
I = np.pi * np.mean(x**4 + np.exp(np.sin(x) + np.cos(x)))  #calculate for given expression 
print(I)
