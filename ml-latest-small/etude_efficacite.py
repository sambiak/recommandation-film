from random import randrange
import os
import numpy as np
import math
import matplotlib.pyplot as plt
from movielens import tableau_des_notes
from recomendation_system_final import descente_du_gradient_2
     
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
            
    return T_validation, L_validation
            
            
def notes_extraites_pour_test(tableau_des_notes_validation,tableau_des_notes_entier):
    """
    :param tableau_des_notes_validation: tableau des notes (moins 10% des notes) utilisé pour optimiser
    :param tableau_des_notes_entier: tableau de notes avec utilisateurs en lignes et films en colonnes
    :return: tableau de notes avec 10% de notes enlevées (pas les mêmes que pour la validation), liste indiquant les couples caractérisant les notes enlevées (utilisateur,film)
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
            
    return T_test, L_test

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
    
def nb_etapes_optimal(mini, V, nb_car, nb_etapes, alpha_X, alpha_theta):
    """
    :param mini: liste indiquant quand est-ce qu'on obtient l'écart minimum
    :param V: tableau de notes (moins 10%)
    :param nb_car: nb de caractéristiques associé à chaque film
    :param nb_etapes: nb d'étapes du gradient à effectuer
    :param alpha_X: valeur de alpha pour la descente du gradient pour X
    :param alpha_theta: valeur de alpha pour la descente du gradient pour theta
    :print: écart quadratique pour un certain nb d'étapes
    :show: graphique écart en fonction du nb_etapes
    :return mini: nouveau minimum
    """
    X = np.random.random((len(tableau_des_notes()[0]), nb_car))
    theta = np.random.random((len(tableau_des_notes()), nb_car))
    x = []
    y = []
    n_etape = 50
    while n_etape <= nb_etapes:
        d = descente_du_gradient_2(X, theta, V[0], nb_car, 50, alpha_X, alpha_theta)
        ecart = ecart_quadratique(V[1],np.dot(d[0],(d[1]).T),tableau_des_notes())
        if ecart < mini[0]:
            mini = [ecart, n_etape, nb_car, alpha_X, alpha_theta]
        print(ecart,"    ",n_etape)
        x += [n_etape]
        y += [ecart]
        X = d[1]
        theta = d[0]
        n_etape += 50
    plt.plot(x,y)
    plt.ylabel('Ecart quadratique')
    nom_x = "Nombre d'étapes  //  nb_car = " + str(nb_car) + " / alpha_X = " + str(alpha_X) + " / alpha_theta = " + str(alpha_theta)
    plt.xlabel(nom_x)
    nom_fichier = "nb_car-" + str(nb_car) + "_alpha_X-" + str(alpha_X) + "_alpha_theta-" + str(alpha_theta) + ".png"
    plt.savefig(nom_fichier)
    plt.show()
        
    return mini
    
V = notes_extraites_pour_validation(tableau_des_notes())
nb_car = 5
alpha_X = 0.001
alpha_theta = 0.0001
mini = [100, 100, nb_car, alpha_X, alpha_theta]

while nb_car <= 150:
    while alpha_X >= 0.000003905:
        while alpha_theta >= 0.0000003905:
            mini = nb_etapes_optimal(mini, V, nb_car, 50, alpha_X, alpha_theta)
            alpha_theta /= 2
        alpha_theta = 0.0001
        alpha_X /= 2
    alpha_X = 0.001
    nb_car += 5
    
print(mini)