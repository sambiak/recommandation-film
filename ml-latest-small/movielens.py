import csv
import numpy as np
import math


def id(titre_du_film):

    """
    fonction id prenant en argument le nom d'un film en chaine de caractères
    et retournant un entier correspondant à l'id de ce film dans movies.csv
    faire attention le titre d'un film contient aussi sa date de parution : par exemple "Toy Story (1995)"
    """

    assert type(titre_du_film) == str

    file = open("movies.csv")
    reader = csv.reader(file)

    for row in reader:
        if row[1] == titre_du_film:
            a = row[0]
            file.close()
            return int(a)

    print("Le film nommé '", titre_du_film, "' n'a pas été trouvé dans la liste de films movies.csv")


def titre(id):

    """
    fonction titre prenant en argument l'id d'un film (entier ou chaine de caractere)
    et retournant en chaine de caractère le titre du film correspondant à l'id dans movies.csv
    """

    assert type(id) == str or type(id) == int

    if type(id) == int:
        id = str(id)

    file = open("movies.csv")
    reader = csv.reader(file)

    for row in reader:
        if row[0] == id:
            a = row[1]
            file.close()
            return a


class Conversions:
    """Classe ayant pour but d'englober les fonctions qui renvoient les donnés avec une
    organisation facilement exploitable.
    """
    def __init__(self):
        file = open("movies.csv")
        reader = csv.reader(file)
        self.dic = {}
        for i, row in enumerate(reader):
            if i != 0:
                self.dic[int(row[0])] = i - 1

    def renvoyer_index(self, id):
        """Fait correspondre a chaque id de film un index"""
        return self.dic[id]


def tableau_des_notes():
    """
        -crée listes array et liste NaN du premier utilisateur(9125)
        -check dans le fichier à partir de la 2eme ligne
        -si l'utilisateur reste le même, à l'index donné par l'id du film, on ajoute la note à la liste de l'utilisateur
        -sinon, on ajoute la liste de l'utilisateur à la liste array, puis on recrée une liste d'utilisateur de NaN
        -et c'est reparti
    
    :return: un array numpy contenant les notes des filmes ordonne avec array[utilisateur][film]
    
    """
    convertisseur = Conversions()
    na_n = float('nan')
    array = []
    file = open("ratings.csv", 'r')
    reader = csv.reader(file)
    liste_par_utilisateur = []
    for i in range(1, 9126):
        liste_par_utilisateur.append(na_n)
    for i, row in enumerate(reader):
        if i == 1:
            dernier_utilisateur = row[0]
        if i != 0:
            if row[0] == dernier_utilisateur:
                liste_par_utilisateur[convertisseur.renvoyer_index(int(row[1]))] = float(row[2])
                dernier_utilisateur = row[0]
            else:
                array.append(liste_par_utilisateur)
                liste_par_utilisateur = []
                for j in range(1, 9126):
                    liste_par_utilisateur.append(na_n)
                dernier_utilisateur = row[0]          

    return np.array(array)
def a_vu_tout_les_films(utilisateur, trié, tableau):
    for i in range(1, 11):
        if math.isnan(tableau[utilisateur,trié[i][1]]):
            return False
    return True
def sous_ensemble():
    tableau = tableau_des_notes()
    réduit = [(tableau[:,i][~np.isnan(tableau[:,i])], i)for i in range(9125)]
    trié = sorted(réduit, reverse=True, key=lambda entrée: len(entrée[0]))
    utilisateurs_ayant_vu_le_premier_film = [i for i, u in enumerate(tableau[:,trié[0][1]]) if not math.isnan(u)]
    utilisateurs_ayant_vu_les_film = [u for u in utilisateurs_ayant_vu_le_premier_film if a_vu_tout_les_films(u, trié, tableau)]
    index_11_premiers_films = [trié[i][1] for i in range(11)]
    tableau_concentré = [[note for i, note in enumerate(tableau[u]) if (i in index_11_premiers_films)] for u in utilisateurs_ayant_vu_les_film]
    return tableau_concentré



def idmin_film_ayant_été_noté_min_n_fois(tableau,n,idminmin,tableau_des_notes):
    for i in range (idminmin,len(tableau_des_notes[1])):
        c=0
        for j in range(len(tableau)):
            if i in tableau[j][1:]:
                c+=1
            if c==n:
                return i
    return False


def tableau_utile(ta):
    tableau_utile=[]
    for i in range(len(ta)):
        tableau_utile+=[[]]
    for i in range(len(ta)):
        for j in range(len(ta[1])):
            if not math.isnan(ta[i,j]):
                tableau_utile[i]+=[j]
        tableau_utile[i]=[i]+tableau_utile[i]
    return tableau_utile


def extraction_de_tableau(tableau,id):
    tableau_extrait=[]
    for i in range(len(tableau)):
        if id in tableau[i][1:]:
            tableau_extrait+=[tableau[i]]
    return tableau_extrait

def meilleur_ss_ensemble_à_n_ligne(ta,n):
    idminmin = 0
    l=[]
    u=[]
    tableau_util=tableau_utile(ta)
    while idminmin<len(ta) and type(idmin_film_ayant_été_noté_min_n_fois(tableau_util,n,idminmin,ta))!=bool:
        idstock=0
        idminmin2=0
        print(idminmin)
        id=idmin_film_ayant_été_noté_min_n_fois(tableau_util,n,idminmin,ta)
        tae=extraction_de_tableau(tableau_util,id)
        while idminmin2<len(ta) and type(idmin_film_ayant_été_noté_min_n_fois(tae,n,idminmin2,ta))!=bool:
            id2=idmin_film_ayant_été_noté_min_n_fois(tae,n,idminmin2,ta)
            tae=extraction_de_tableau(tae,id2)
            à_enlever=[]
            for i in range (len(tae)):
                for j in range(1,len(tae[i])):
                    if tae[i][j]<id2 and tae[i][j]>=idstock:
                        à_enlever+=[[i,j]]
                    elif tae[i][j]>=id2:
                        break
            for i in range (len(à_enlever)):
                del tae[à_enlever[i][0]][à_enlever[i][1]]
                for j in range(i+1,len(à_enlever)):
                    if à_enlever[j][0]==à_enlever[i][0]:
                        à_enlever[j][1]=à_enlever[j][1]-1
                    else:
                        break
            idstock=id2+1
            idminmin2=id2+1
        àeff=[]
        for i in range (len(tae)):
            for j in range (1,len(tae[i])):
                if tae[i][j]==id2:
                    àeff+=[[i,j+1]]
                    break
        for i in range(len(àeff)):
            del tae[àeff[i][0]][àeff[i][1]:]
        l2=[]
        u2=[]
        for i in tae[0][1:]:
            l2+=[i]
        for i in range (len(tae)):
            u2+=[tae[i][0]]
        if len(l2)>len(l):
            l=[]
            u=[]
            for i in l2:
                l+=[i]
            for i in u2:
                u+=[i]
        idminmin=id+1
    tae=[]
    for i in range (len(u)):
        tae+=[[]]
    for i in range(len(u)):
        for j in range (len(l)):
            tae[i]+=[ta[u[i]][l[j]]]
    na_n = float('nan')
    l=[na_n]+l
    for i in range (len(u)):
        tae[i]=[u[i]]+tae[i]
    tae=[l]+tae
    return tae

def ss_ensemble_avec_le_plus_de_colonnes_possible_et_minimum_n_lignes(n,tableau_des_notes):
    j=0
    tae=[[]]
    while len(tae[0])>=j:
        j=len(tae[0])
        tae=meilleur_ss_ensemble_à_n_ligne(tableau_des_notes,n)
        n+=1
    return meilleur_ss_ensemble_à_n_ligne(tableau_des_notes,n-2)


def tableau_bricolé_de_l_lignes_et_c_colonnes(tableau_des_notes,l,c):
    num_ligne = []
    num_colonne = []
    nb_de_notes=[]
    for i in range (len(tableau_des_notes)):
        compte=0
        for note in tableau_des_notes[i]:
            if not math.isnan(note):
                compte+=1
        if len(num_ligne)<l:
            nb_de_notes.append(compte)
            num_ligne.append(i)
        elif compte > min(nb_de_notes):
            a = nb_de_notes.index(min(nb_de_notes))
            nb_de_notes[a] = compte
            num_ligne[a] = i
    tableau_bricolé=tableau_des_notes.take(num_ligne,axis=0)
    nb_de_notes = []
    for i in range (len(tableau_bricolé[0])):
        compte=0
        for j in range (len(tableau_bricolé)):
            if not math.isnan(tableau_bricolé[j][i]):
                compte+=1
        if len(num_colonne)<c:
            nb_de_notes.append(compte)
            num_colonne.append(i)
        elif compte>min(nb_de_notes):
            a=nb_de_notes.index(min(nb_de_notes))
            nb_de_notes[a]=compte
            num_colonne[a]=i
    return tableau_bricolé.take(num_colonne,axis=1)
