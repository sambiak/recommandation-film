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


def id_film(index):
    """
    :param index: index du film dans tableau des notes
    :return: l'id du film dans le fichier movies.csv
    """
    file = open("movies.csv")
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i-1==index:
            file.close()
            return(row[0])


class Conversions:
    """Classe ayant pour but d'englober les fonctions qui renvoient les donnés avec une
    organisation facilement exploitable.
    """
    def __init__(self):
        file = open("movies.csv")
        reader = csv.reader(file)
        self.dic = {}
        self.noms = {}
        self.donnes = []
        for i, row in enumerate(reader):
            if i != 0:
                self.dic[int(row[0])] = i - 1
                self.donnes.append((int(row[0]),row[1]))
                self.noms[int(row[0])] = row[1]
        file.close()

    def renvoyer_index(self, id):
        """Fait correspondre a chaque id de film un index de 0 à nombre filmes"""
        return self.dic[id]

    def renvoyer_id(self, index):
        """Fait l'inverse de renvoyer index"""
        return  self.donnes[index][0]

    def renvoyer_nom_index(self, index):
        """renvoie le nom du film a l'index indiqué"""
        return self.donnes[index][1]

    def renvoyer_nom_id(self, id):
        """Renvoie le nom du film qui a cette movieId"""
        return self.noms[id]


def nombre_films():
    return 9125


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
        if math.isnan(tableau[utilisateur ,trié[i][1]]):
            return False
    return True


def sous_ensemble():
    """Renvoie un sous_tableau sans nan en regardant les films les plus regardés et prend les utlisateurs present dans ces films"""
    tableau = tableau_des_notes()
    réduit = [(tableau[:,i][~np.isnan(tableau[:,i])], i) for i in range(9125)]
    trié = sorted(réduit, reverse=True, key=lambda entrée: len(entrée[0]))
    utilisateurs_ayant_vu_le_premier_film = [i for i, u in enumerate(tableau[: ,trié[0][1]]) if not math.isnan(u)]
    utilisateurs_ayant_vu_les_film = [u for u in utilisateurs_ayant_vu_le_premier_film if a_vu_tout_les_films(u, trié, tableau)]
    index_11_premiers_films = [trié[i][1] for i in range(11)]
    tableau_concentré = [[note for i, note in enumerate(tableau[u]) if (i in index_11_premiers_films)] for u in utilisateurs_ayant_vu_les_film]
    return tableau_concentré


def tableau_bricolé_de_l_lignes_et_c_colonnes(tableau_des_notes,l,c):
    # renvoie un tableau extrait qui comporte peu de nan, c pas optimal mais c pas mal
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
    return tableau_bricolé.take(num_colonne,axis=1), num_colonne, num_ligne


