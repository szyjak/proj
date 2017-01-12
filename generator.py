import numpy as np
import matplotlib.pyplot as plt


def range_flo(range=2000, loc=5, scale=2):
    rng = np.random.RandomState(10)  # deterministic random data
    a = np.hstack((rng.normal(size=range/2),
               rng.normal(loc, scale, size=range/2)))
    return a

def range_int():



if __name__=="__main__":
    b=str(gaus_flo())
    print  b
