import csv
import numpy as np
import math


#liste des films
#liste des id des films : id[6] c'est l'id du film rangé à films[6]

file = open("movies.csv","r")
reader = csv.reader(file)

movies=[]
id_o=[]


for row in reader:
    movies.append(row[1])
    id_o.append(row[0])


del movies[0]
del id_o[0]

file.close()




file2 = open("ratings.csv","r")
reader2 = csv.reader(file2)

users=[]
ratings=[]
movieId=[]



for row in reader2:
    users.append(row[0])
    ratings.append(row[2])
    movieId.append(row[1])


del users[0]
del ratings[0]
del movieId[0]


n_user = []
for i, usert in enumerate(users):
    user = int(usert)
    if user > len(n_user):
        n_user.append({})
    n_user[user-1][movieId[i]]= ratings[i]

id={}
for i, truc in enumerate(movies):
    id[movies[i]] = id_o[i]


movie_id={}
for i, machin in enumerate(id_o):
    movie_id[id_o[i]] = movies[i]


file2.close()



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

    assert type(id) == str or type(id)==int

    if type(id) == int:
        id=str(id)

    file = open("movies.csv")
    reader = csv.reader(file)

    for row in reader:
        if row[0] == id:
            a = row[1]
            file.close()
            return a



class conversions():
    def __init__(self):
        file = open("movies.csv")
        reader = csv.reader(file)
        self.dic = {}
        for i, row in enumerate(reader):
            if i != 0:
                self.dic[int(row[0])] = i - 1

    def renvoyer_index(self, id):
        return self.dic[id]

    print("Aucun film ne correspond à l'id", id, "dans movies.csv")

def tableau_des_notes():
    """
    pour gerer les Nan utilise math.isnan
        -crée listes array et liste NaN du premier utilisateur(9125)
        -check dans le fichier à partir de la 2eme ligne
        -si l'utilisateur reste le même, à l'index donné par l'id du film, on ajoute la note à la liste de l'utilisateur
        -sinon, on ajoute la liste de l'utilisateur à la liste array, puis on recrée une liste d'utilisateur de NaN
        -et c'est reparti
    
    :return: un array numpy contenant les notes des filmes ordonne avec array[utilisateur][film]
    """
    convertisseur = conversions()
    NaN = math.nan
    
    array = []
    
    liste_par_utilisateur = []
    file = open("ratings.csv","r")
    reader = csv.reader(file)
    liste_par_utilisateur = []
    for i in range (1,9126):
        liste_par_utilisateur.append(NaN)
    for i ,row in enumerate(reader):
        if i == 1:
            dernier_utilisateur = row[0]
        if i != 0:
            if row[0] == dernier_utilisateur:
                liste_par_utilisateur[convertisseur.renvoyer_index(int(row[1]))] = row[2]
                dernier_utilisateur = row[0]
            else:
                array.append(liste_par_utilisateur)
                liste_par_utilisateur = []
                for i in range (1,9126):
                    liste_par_utilisateur.append(NaN)
                dernier_utilisateur = row[0]          

    return np.array(array)

def moyennedesnotesparfilm(tableau_des_notes()):
    moy=0
    list_moy=[]
    k=0
    for i in range(9125):
        for j in np.array(array)  :
            moy+=j[i]
            k+=1
        moy=moy/k
        list_moy+=[moy]
    return list_moy

print(moyennedesnotesparfilm(tableau_des_notes()))



