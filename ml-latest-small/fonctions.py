from movielens import sous_ensemble
import numpy as np
import math
def moyenne_des_notes_des_film(array):
    """renvoit la liste des moyennes des notes par film en prenant le tableau des notes"""
    list_moy = []
    k=0
    moy=0
    for i in range(9125):
        for j in (array[:,i]):
            if not math.isnan(j) :
                k+=1
                moy+=j
        if k==0:
            list_moy += [math.nan]
        else:
            list_moy += [moy/k]
    return list_moy
  
