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


def moyenne_des_notes_par_film(fonction):
    """renvoit la liste des moyennes des notes par film en prenant le tableau des notes"""
    moy = 0
    list_moy = []
    k = 0
    for i in range(9125):
        for j in fonction:
            if not math.isnan(float(j[i])):            
                moy += j[i]
                k += 1
        if k != 0:
            moy = moy / k
        else:
            moy = float('nan')
        list_moy += [moy]
    return list_moy

print(moyenne_des_notes_par_film(tableau_des_notes()))
