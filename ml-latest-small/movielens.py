import csv

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

print(movie_id)

file2.close()

