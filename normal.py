# -*- coding: utf-8 -*-
import numpy as np
import math
import hist

#2^8=256
# (2^8)^4=4.294.967.296 -lisc opcji na 4 bajtach
# (2^8)^4=18.446.744.073.709.551.616 8B  
# 16184#

#funkcja budująca wstępny histogram:
#pobiera wektor danych, ilość pików na histogramie i zakres danych
def hist_wstep(input,p,zakres):
 #robie histogram o p-pikach 
# czyli wektor o dł = ilość pików p
    histogram=np.zeros(p)
    wsp=zakres/p #wsp będzie int w dół
#przebiegając po input[] buduję histogram
#wiedząc z góry jaki jest zakres zmiennej i ile pików ma mieć histogram
    for x in input:
        histogram[x*p/zakres]+=1
#dziele wartość z pierwotnego zbioru i dziele przez zakres oraz mnoze przez p
#i do tej kolumny histogramu dodaję 1
    hist.rysuj(histogram)


# zadaniem funkcji powinno być odczytać część pliku, obliczyć wsp na podstawie pierwszych 2 GB
#nstępnie wybrać interesujący zakres i znormalizować histogram


#ta funkcja przelicza wartość jednej danej zgodnie z wyborem użytkownika
# wybieramy górny i dolny zakres danych następnie tylko ten przedział skaluje na 8-bit
# narazia zamiast 8b-256 dam zmienną zakres_out 
def normlizuj(x, up, down,zakres_out):
    y=0
    if x>down and x<up:
        y=x*(up-down)*zakres_out
    #else y=0
    return y
#wygląda nieźle, ale trzeba potestować…
