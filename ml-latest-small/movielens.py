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




ta=tableau_des_notes()


def idmin_film_ayant_été_noté_min_n_fois(tableau,n,idminmin):
    for i in range (idminmin,len(ta[0])):
        c=0
        for j in range(len(tableau)):
            if i in tableau[j][1:]:
                c+=1
        if c>=n:
            return [i,c]
    return False


def tableau_utile(ta):
    tableau_utile=[]
    for i in range(len(ta)):
        tableau_utile+=[[]]
    for i in range(len(ta)):
        for j in range(len(ta[0])):
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
    idminmin2 = 0
    l=[]
    tableau_util=tableau_utile(ta)
    while idminmin<len(ta) and type(idmin_film_ayant_été_noté_min_n_fois(tableau_util,n,idminmin))!=bool:
        print(idminmin)
        id=idmin_film_ayant_été_noté_min_n_fois(tableau_util,n,idminmin)
        tae=extraction_de_tableau(tableau_util,id[0])
        while idminmin2<len(ta) and type(idmin_film_ayant_été_noté_min_n_fois(tae,n,idminmin2))!=bool:
            id2=idmin_film_ayant_été_noté_min_n_fois(tae,n,idminmin2)
            tae=extraction_de_tableau(tae,id2[0])
            idminmin2=id2[0]+1
        l2=[]
        for i in tae[0][1:]:
            l2+=[i]
        if len(l2)>len(l):
            l=[]
            for i in l2:
                l+=[i]
        idminmin=id[0]+1
    return(l)

""""meilleur_ss_ensemble_à_n_ligne(ta,180) renvoie une liste de 1699 id de films qui ont tous étés notés 180 fois par les memes utilissateurs
à mon avis c le meilleur tableau extrait kon peut trouver meme si ça reste a vérifier"""
