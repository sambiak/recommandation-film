from random import *
import numpy as np
import math
from movielens import tableau_des_notes
from recomendation_system_final import *

def pourcentage_de_non_nan(array): 
    k=0 
    for i in range(9125): 
        for j in array[:,i]: 
            if not math.isnan(j) : 
                k+=1 
    return k/(9125*670) 
     
def nbre_de_film_vu_par_utilisateur(array,i): 
    k=0 
    for j in array[i,:]: 
        if not math.isnan(j) : 
            k+=1 
    return k 

def notes_extraites_pour_validation(tableau_des_notes_entier):
    """fonction qui
    """
    
    na_n = float('nan')
    T_validation=tableau_des_notes_entier.copy()
    L_validation = []
    
    for n_eme_note_de_validation in range (9922):
        numero_utilisateur = randrange (0,670)
        while nbre_de_film_vu_par_utilisateur(tableau_des_notes_entier,numero_utilisateur) < 10: 
            numero_utilisateur = randrange (0,670) 
        numero_film = randrange (1,9125) 
        compteur = [0,0]
        for i, film in enumerate(T_validation[numero_utilisateur]): 
            if not math.isnan(film): 
                compteur = [compteur[0]+1,i]
                if compteur[0] == numero_film:
                    film = na_n
                    compteur = [0,0]
                    L_validation.append([numero_utilisateur,i])
                    break
        if compteur[0] != 0: 
            T_validation[numero_utilisateur][compteur[1]] = na_n 
            L_validation.append([numero_utilisateur,compteur[1]])
            compteur = [0,0]
            
    return [T_validation,L_validation]
            
            
def notes_extraites_pour_test(tableau_des_notes_validation,tableau_des_notes_entier):
    na_n = float('nan')
    T_validation = tableau_des_notes_validation.copy()
    T_test=tableau_des_notes_entier.copy()    
    L_test = []
    
    for n_eme_note_de_validation in range (9922):
        numero_utilisateur = randrange (0,670)
        while nbre_de_film_vu_par_utilisateur(tableau_des_notes_validation,numero_utilisateur) < 10: 
            numero_utilisateur = randrange (0,670) 
        numero_film = randrange (1,9125) 
        compteur = [0,0]
        for i, film in enumerate(T_validation[numero_utilisateur]): 
            if not math.isnan (film): 
                compteur = [compteur[0]+1,i]
                if compteur[0] == numero_film:
                    T_test[numero_utilisateur][i] = na_n
                    compteur = [0,0]
                    L_test.append([numero_utilisateur,i]) 
                    break
        if compteur[0] != 0:
            T_test[numero_utilisateur][compteur[1]] = na_n
            L_test.append([numero_utilisateur,compteur[1]])
            compteur = [0,0]
            
    return [T_test,L_test]

def ecart_quadratique(L_notes_enlevees,Y_predit,tableau_des_notes_entier): 
    somme = 0
    for note in L_notes_enlevees:
        somme+= (Y_predit[note[0]][note[1]]-tableau_des_notes_entier[note[0]][note[1]])**2
    
    return somme/9922
    
def nb_car_optimal():
    L_ecarts = []
    n = notes_extraites_pour_validation(tableau_des_notes())
    i=2**3 
    while i!=2**5: 
        d = descente_du_gradient(n[0],i,500,0.001, 0.0001) 
        ecart = ecart_quadratique(n[1],np.dot(d[1],(d[0]).T),tableau_des_notes())
        print(ecart)
        L_ecarts += [i,ecart] 
        i+=4 
    
    return L_ecarts

print(nb_car_optimal())