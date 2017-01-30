import csv

#liste des films
#liste des id des films : id[6] c'est l'id du film rangé à films[10]

file = open("movies.csv","r")
reader = csv.reader(file)

movies=[]
id=[]


for row in reader:
    movies = movies + [row[1]]
    id=id+[row[0]]


del movies[0]
del id[0]

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

file2.close()

