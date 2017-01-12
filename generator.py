# -*- coding: utf-8 -*-
import random
import math
from random import gauss #as gauss

def range_f(range=10,up=1024,down=0):
    values = []
    sigma=(up-down)*0.15 # w miarę spoko
    while len(values) < range:
        value = gauss((up+down)/2, sigma)
        if down < value < up:
            values.append(value)
    return values

def range_i(range=10,up=1024,down=0):
    values = []
    sigma=(up-down)*0.15 # w miarę spoko
    while len(values) < range:
        value = int(gauss((up+down)/2, sigma))
        if down < value < up:
            values.append(value)
    return values

def range2_i(range=10,up=1024,down=0):
    w1=range_i(range/2,up/2,down)
    w2=range_i(range/2,up,up/2)
    w1.extend(w2)
    return w1

def range_n_i(r=100,up=1024,down=0,n=5):
    ret= []
    for x in range(n):
        w=range_i(r/n,(x+1)*(up/n),x*(up/n))#…
        ret.extend(w)
    return ret

def rand(range=10,up=1024,down=0):
    values = []
    while len(values) <range:
        value= random.randint(down, up)

if __name__=="__main__":
    b=str(range_f())
    c=str(range_i())
    print  b+"\n"+c
