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




# fonction id prenant en argument le nom d'un film en chaine de caractères
# et retournant un entier correspondant à l'id de ce film dans movies.csv
# faire attention le titre d'un film contient aussi sa date de parution : par exemple "Toy Story (1995)"

def id(titre_du_film):

    assert type(titre_du_film) == str

    file = open("movies.csv")
    reader = csv.reader(file)

    for row in reader:
        if row[1] == titre_du_film:
            a = row[0]
            file.close()
            return int(a)

    print("Le film nommé '", titre_du_film, "' n'a pas été trouvé dans la liste de films movies.csv")



# fonction titre prenant en argument l'id d'un film (entier ou chaine de caractere)
# et retournant en chaine de caractère le titre du film correspondant à l'id dans movies.csv

def titre(id):

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

    print("Aucun film ne correspond à l'id", id, "dans movies.csv")
def tableau_des_notes():
    """
    Fonction temporaire pour commencer a travailler sur d'autres parties du projet
    ne renvoit pas un tableau correspondant a quoi que ce soit de reelle
    pour gerer les Nan utilise math.isnan
    :return: un array numpy contenant les notes des filmes ordonne avec array[utilisateur][film]
    """
    NaN = math.nan
    return np.array([[4.0, NaN, 3.0, 2.0, 4.5, NaN, 3.5],[3.5, 4.5, NaN, 2.0, 4.5, NaN, 4.5], [5.0, 5.0, 4.0, 2.0, 2.5, 5.0, 3.5]])





