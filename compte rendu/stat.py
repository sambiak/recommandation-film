from math import *
import numpy as np
from movielens import *
import matplotlib.pyplot as plt


#renvoi une liste donnant le nombre de film vu par chaque utilisateur
def nbre_de_film_vu_par_utilisateur(array):
    film_vu=[]
    for i in range(670):
        k=0
        for j in array[i,:]:
            if not math.isnan(j) :
                k+=1
        film_vu+=[k]
    return film_vu

#retourne une liste contenant le nombre de fois qu'a ete note chaque film
def nbre_de_note_par_film(array):
    film_note=[]
    for i in range(9125) :
        k=0
        for j in array[:,i]:
            if not math.isnan(j):
                k+=1
        film_note+=[k]
    return film_note


#donne le pourcentage de NaN pour le cas de notre tableau des notes(98,4%)
def pourcentage_de_nan(array):
    k=0
    for i in range(9125):
        for j in array[:,i]:
            if not math.isnan(j) :
                k+=1
    return k/(9125*670)


#la personne qui a note le plus de film en a note 2390
#le film qui a le plus de note en a 339





