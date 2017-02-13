from movielens import *
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


#renvoi une liste donnant le nombre de film vu par utilisateur
def nbre_de_film_vu_par_utilisateur(array):
    film_vu=[]
    for i in range(670):
        k=0
        for j in array[i,:]:
            if not math.isnan(j) :
                k+=1
        film_vu+=[k]
    return film_vu


#retourne le nombre de fois qu'a ete note un film
def nbre_de_note_par_film(array):
    film_note=[]
    for i in range(9125) :
        k=0
        for j in array[:,i]:
            if not math.isnan(j):
                k+=1
        film_note+=[k]
    return film_note

#compte le nombre de personnes ayant vu plus de 500film
p=0
for i in nbre_de_film_vu_par_utilisateur(tableau_des_notes())  :
    if i>500 :
        p+=1
print(p)


#compte le nombre de film ayant ete note par plus de 100 utilisateurs
q=0
for i in nbre_de_note_par_film(tableau_des_notes()) :
    if i>100 :
        q+=1
print(q)


print(nbre_de_note_par_film(tableau_des_notes()))
print(nbre_de_film_vu_par_utilisateur(tableau_des_notes()))





