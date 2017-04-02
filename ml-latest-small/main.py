from utilisateur import Utilisateur
from movielens import tableau_des_notes
from recomendation_system_final import descente_du_gradient
import pickle

fan_de_animation = Utilisateur()
fan_de_animation.ajout_film(1, 5)
fan_de_animation.ajout_film(4306, 5)
fan_de_animation.ajout_film(3114, 5)
fan_de_animation.ajout_film(76093, 5)
fan_de_animation.ajout_film(79091, 5)
fan_de_animation.ajout_film(81564, 5)#mega_mind
fan_de_animation.ajout_film(81847, 5)#tangled
fan_de_animation.ajout_film(84944, 4)#rango
fan_de_animation.ajout_film(86298, 5)#rio
fan_de_animation.ajout_film(87222, 5)#kung fu panda 2
fan_de_animation.ajout_film(87876, 5)#cars 2
fan_de_animation.ajout_film(90647, 5)#puss in boots
fan_de_animation.ajout_film(91500, 0)
fan_de_animation.ajout_film(91890, 0)#iron lady the
fan_de_animation.ajout_film(92058, 0)#Human Centipede II (Full Sequence), The
fan_de_animation.ajout_film(95207, 0)#Abraham Lincoln: Vampire Hunter
fan_de_animation.ajout_film(96691, 0)#Resident Evil: Retribution
fan_de_animation.ajout_film(103249, 0)#World War Z (2013)





Y=tableau_des_notes()
theta, X = descente_du_gradient(Y, 50, 1000, 0.0001, 0.00001)
fan_de_animation.theta(X, 40000)
pickle.dump( fan_de_animation, open( "save.p", "wb" ) )
pickle.dump(X, open( "save2.p", "wb" ))
print(fan_de_animation.reccomandation(X))
t2 = pickle.load( open( "save.p", "rb" ) )
print(t2.reccomandation(X))
