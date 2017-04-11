from random import randrange
import numpy as np
import math
from movielens import tableau_des_notes
from recomendation_system_final import descente_du_gradient

def pourcentage_de_non_nan(array):
    """
    :param array: tableau de notes avec utilisateurs en lignes et films en colonnes
    :return: pourcentage de notes (on différencie les notes et les "nan")
    """
    k=0 
    for i in range(9125): 
        for j in array[:,i]: 
            if not math.isnan(j) : 
                k+=1 
    return k/(9125*670) 
     
def nbre_de_film_vu_par_utilisateur(array,i): 
    """
    :param array: tableau de notes avec utilisateurs en lignes et films en colonnes
    :param i: ième utilisateur
    :return: nb de films vu par l'utilisateur
    """
    k=0 
    for j in array[i,:]: 
        if not math.isnan(j) : 
            k+=1 
    return k 

def notes_extraites_pour_validation(tableau_des_notes_entier):
    """
    :param tableau_des_notes_entier: tableau de notes avec utilisateurs en lignes et films en colonnes
    :return: tableau de notes avec 10% des notes enlevées(tableau de validation), liste indiquant les couples caractérisant les notes enlevées (utilisateur,film)
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
    """
    :param tableau_des_notes_validation: tableau des notes moins 10% des notes utilisé pour optimiser
    :param tableau_des_notes_entier: tableau de notes avec utilisateurs en lignes et films en colonnes
    :return: tableau de notes avec 10% de notes enlevées(pas les mêmes que pour la validation), liste indiquant les couples caractérisant les notes enlevées (utilisateur,film)
    """
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
    """
    :param L_notes_enlevees: liste de couples caractérisant les notes enlevées du tableau (utilisateur,film)
    :param Y_predit: tableau de notes plein avec prédiction par descente du gradient à partir du tableau de validation
    :param tableau_des_notes_entier: tableau de notes avec utilisateurs en lignes et films en colonnes (tableau de départ)
    """
    somme = 0
    for note in L_notes_enlevees:
        somme+= (Y_predit[note[0]][note[1]]-tableau_des_notes_entier[note[0]][note[1]])**2
    
    return somme/9922
    
def nb_car_optimal():
    """
    :print: écart quadratique pour un certain nb de caractéristiques
    :return: liste avec tous les écarts calculés en fonction du nb de caractéristiques
    """
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