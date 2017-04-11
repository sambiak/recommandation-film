from random import *
import numpy as np
import math
from movielens import tableau_des_notes
from recomendation_system_final import *

def notes_extraites_pour_validation(tableau_des_notes_entier):
    na_n = float('nan')
    T_validation=tableau_des_notes_entier.copy()
    L_validation = []
    
    for n_eme_note_de_validation in range (9922):
        numero_utilisateur = randrange (0,670)
        numero_film = randrange (1,2391)
        compteur = [0,0]
        for i in range(len (T_validation[numero_utilisateur])):
            if not math.isnan (T_validation[numero_utilisateur][i]):
                compteur = [compteur[0]+1,i]
                if compteur[0] == numero_film:
                    T_validation[numero_utilisateur][i] = na_n
                    compteur = [0,0]
                    L_validation += [numero_utilisateur,i]
                    break
        if compteur[0]!=0:
            T_validation[numero_utilisateur][compteur[1]] = na_n
            compteur = [0,0]
            L_validation += [numero_utilisateur,compteur[1]]
            
    return [T_validation,L_validation]
            
            
def notes_extraites_pour_test(tableau_des_notes_validation,tableau_des_notes_entier):
    na_n = float('nan')
    T_validation = tableau_des_notes_validation.copy()
    T_test=tableau_des_notes_entier.copy()    
    L_test = []
    
    for n_eme_note_de_validation in range (9922):
        numero_utilisateur = randrange (0,670)
        numero_film = randrange (1,2391)
        compteur = [0,0]
        for i in range(len (T_validation[numero_utilisateur])):
            if not math.isnan (T_validation[numero_utilisateur][i]):
                compteur = [compteur[0]+1,i]
                if compteur[0] == numero_film:
                    T_test[numero_utilisateur][i] = na_n
                    compteur = [0,0]
                    L_test += [numero_utilisateur,i]
                    break
        if compteur[0] != 0:
            T_test[numero_utilisateur][compteur[1]] = na_n
            compteur = [0,0]
            L_test += [numero_utilisateur,compteur[1]]
            
    return [T_test,L_test]

def ecart_moyen(L_notes_enlevees,Y_predit,tableau_des_notes_entier):
    somme = 0
    for note in L_notes_enlevees:
        somme+= abs(Y_predit[note[0]][note[1]]-tableau_des_notes_entier[note[0]][note[1]])
    
    return somme/9922
    
def nb_car_optimal():
    L_ecarts = []
    n = notes_extraites_pour_validation(tableau_des_notes())
    for puissance in range (0,8):
        d = descente_du_gradient(n[0],2**puissance,5000,0.001, 0.0001)
        ecart = ecart_moyen(n[1],np.dot(d[0],(d[1]).T),tableau_des_notes)
        print(ecart)
        L_ecarts += [2**puissance,ecart]
    
    return L_ecarts

print(nb_car_optimal())