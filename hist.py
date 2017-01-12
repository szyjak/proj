# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#funkcja rysuje takie słupki jakie dostanie na input, nic nie przelicza!
def rysuj(histogram):
    p= len(histogram) #ilość supków
    pozycja = np.arange(p)  # położenia słupków na osi x
    szer = 0.99#0.8       # szer słupka jako ułamek

    fig, ax = plt.subplots()
    supki = ax.bar(pozycja, histogram, szer, color='b')

    ax.set_ylabel('zliczenia') 
    ax.set_title('histogram') 
    plt.show()

#można ustawiać etykietki ale automat leci dobrze
    #ax.set_xticks(pozycja+0.5)# 0.5 ustawia tick w połowie słupka
    #ax.set_xticklabels(range(p)) #nawet nawet


