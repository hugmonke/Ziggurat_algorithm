import ziggurat as zig
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st 

if __name__ == "__main__":
    n = 100000
    sol, alpha = zig.generate(n)
    b=0
    if alpha == 1:
        b = 2000
    else: 
        b = 200
    plt.title("Pareto Distribution - Ziggurat vs theoretical")
    plt.ylabel("Density function f(x)")
    plt.xlabel("x")
    plt.hist(sol, bins = b, density = True)
    plt.xlim([1, 10])

    x = np.linspace(1, 10, 1000)
    y = st.pareto.pdf(x, alpha)

    XX = np.linspace(1, 10, 1000)
    YY = st.pareto.cdf(x, alpha)
    summ = np.zeros(n)
    summ = np.arange(len(sol))/len(sol)


    #If alpha = 1 st.pareto.mean(alpha) returns inf, if alpha > 1 st.pareto.mean(alpha) returns correct expected values
    ex1 = np.mean(sol)
    ex2 = st.pareto.mean(alpha)

    var1 = np.var(sol)
    var2 = st.pareto.var(alpha)

    print("Empirical expected value ", ex1, "\nTheoretical expected value ", ex2)
    print("empirical variance ", var1, "\ntheoretical variance: ", var2)
    plt.plot(x, y, label = "Theoretical distribution")
    plt.legend()
    plt.show()

    plt.title("Pareto Distribution - Ziggurat vs theoretical")
    plt.plot(np.sort(sol), summ, label = "ECDF")
    plt.plot(XX, YY, label = "Theoretical CDF")
    plt.legend()
    plt.ylabel("CDF")
    plt.xlabel("x")
    plt.show()
