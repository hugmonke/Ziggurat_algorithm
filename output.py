import ziggurat as zig
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st 

if __name__ == "__main__":
    n = 100000
    wyn, alfa = zig.generate(n)
    b=0
    if alfa == 1:
        b = 2000
    else: 
        b = 200
    plt.title("Pareto Distribution - Ziggurat vs theoretical")
    plt.ylabel("Density function f(x)")
    plt.xlabel("x")
    plt.hist(wyn, bins = b, density = True)
    plt.xlim([1, 10])

    x = np.linspace(1, 10, 1000)
    y = st.pareto.pdf(x, alfa)

    iks = np.linspace(1, 10, 1000)
    igrek = st.pareto.cdf(x, alfa)
    sumka = np.zeros(100000)
    sumka = np.arange(len(wyn))/len(wyn)


    #If alfa = 1 st.pareto.mean(alfa) returns inf, if alfa > 1 st.pareto.mean(alfa) returns correct expected values
    ex1 = np.mean(wyn)
    ex2 = st.pareto.mean(alfa)

    var1 = np.var(wyn)
    var2 = st.pareto.var(alfa)

    print("Empirical expected value ", ex1, "\nTheoretical expected value ", ex2)
    print("empirical variance ", var1, "\ntheoretical variance: ", var2)
    plt.plot(x, y, label = "Theoretical distribution")
    plt.legend()
    plt.show()

    plt.title("Pareto Distribution - Ziggurat vs theoretical")
    plt.plot(np.sort(wyn), sumka, label = "ECDF")
    plt.plot(iks, igrek, label = "Theoretical CDF")
    plt.legend()
    plt.ylabel("CDF")
    plt.xlabel("x")
    plt.show()