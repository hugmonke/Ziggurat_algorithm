#Ziggurat Algorithm for generating random variables with Pareto distribution

import numpy as np

    
def f(x, alfa, Xm):
    return alfa*(Xm**alfa)/(x**(alfa+1))


def f_reversed(x, alfa, Xm): 
    return (alfa/x)**(1/(alfa+1))


def integral(r, alfa, Xm):
    return (Xm/r)**(alfa)


def z(r, alfa, Xm):
    """z(r) function - return difference of area and tail"""
    xlist = np.zeros(256)
    xlist[255] = r
    v = f(r, alfa, Xm) * r + integral(r, alfa, Xm)
    
    for i in range(254, -1, -1):
        xlist[i] = f_reversed((v/xlist[i+1] + f(xlist[i+1], alfa, Xm)), alfa, Xm)
    return (v-xlist[0] + (xlist[0] * f(xlist[0], alfa, Xm))), xlist
    
    
def calc_r(alpha, Xm):
    """Bisection method to find r value"""

    r1 = 1000
    r2 = 0

    while abs(r1-r2) > 0.000001: 
        x1 = (r1+r2)/2

        if abs(z(x1, alpha, Xm)[0]) <= 0.000001:
            break
        elif z(x1, alpha, Xm)[0] * z(r1, alpha, Xm)[0] < 0:
            r2 = x1
        else:
            r1 = x1

    return x1, z(x1, alpha, Xm)[1]


def generate(n):
    #input
    while True:
        try:
            alpha = float(input("Input shape parameter alpha >= 1: "))
        except ValueError:
            print("Input correct data type!\n")
            continue
        if alpha < 1:
            print("Alpha must be greater than 1!")
            continue
        else:
            break
    Xm = 1

    #generator 
    def pareto():
        """Generator - returns random variables"""
        j = np.random.uniform(0,1)
        i = int(np.random.uniform(0, 256))
        scale = ((1/alpha)**(1/(alpha+1)))
        x = scale*length[i]

        if j <= ratio[i]:
            return x 
        else:
            while True:
                if i == 0: 
                    return r_max + f_reversed(U, alpha, Xm) 
                x = length[i] 

                if (j*(func_val[i-1]-func_val[i]) + func_val[i] < f(x, alpha, Xm)): 
                    return scale*x 
                j = np.random.uniform(0,1)
                i = int(np.random.uniform(0, 256))

    #tables setup  
    ratio = np.zeros(256) #(x_i-1/x_i)
    length = np.zeros(256) #x_i
    func_val = np.zeros(256)
    wyn = np.zeros(n)
    
    r_max, xlist = calc_r(alpha, Xm) 
    
    area = r_max*f(r_max, alpha, Xm) + integral(r_max, alpha, Xm) #one rectangle area
    
    tail_length = area/f(r_max, alpha, Xm)

    ratio[0] = (r_max/tail_length)
    
    length = xlist

    func_val[0] = alpha*(Xm**alpha)
    func_val[255] = f(r_max, alpha, Xm)

    U = np.random.uniform(0,1)
    
    
    #calculates x_i-1/x_i (ratio)
    #calculates func_results
    #calculates length using calc_r
    for i in range(254, 0, -1):
        
        ratio[i] = (xlist[i]/xlist[i+1])          
        func_val[i] = f(xlist[i], alpha, Xm) 
        
        
    #generating n variables  
    for h in range(0, n):  
        wyn[h] = pareto()
        
    return wyn, alpha


