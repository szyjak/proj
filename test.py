# -*- coding: utf-8 -*-
#POLSKIE ZNAKI!!!! ąęół

import generator as g
import math
import hist
import normal as n

#2^8=256
# (2^8)^4=4.294.967.296 -lisc opcji na 4 bajtach
# (2^8)^4=18.446.744.073.709.551.616 8B  
# 16184#
zakres=pow(pow(2,8),4)
wec_int=g.range_n_i(1000000,zakres,0,2) # 10krandomów z zakresu int
# teraz chcę zapisać całą rzecz jako bin bez rozdrabniania na LE i BE
# potem wczytać i przeskalować
n.hist_wstep(wec_int,256,zakres)# dziła ładnie
# teraz 
#narysuj hist z pierwszych 2% danych, wybierz up i down , normalizuj dane funkcją
#i jebnij histogram
#powinno być git

