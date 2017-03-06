import numpy as np
from movielens import sous_ensemble

def h_theta(theta, x_i):
    valeur = theta[0]
    for theta_j, x_i_j in zip(theta[1:], x_i):
        valeur += theta_j * x_i_j
    return valeur


def fonction_cout(theta, x, y):
    cout = 0
    for x_i, y_i in zip(x, y):
        cout += (h_theta(theta, x_i) - y_i) ** 2
    return cout / (2 * len(y))


def derivée_partielle_par_rapport_à_theta_j(j, theta, x, y):
    valeur = 0
    for i in range(len(x)):
        valeur += (h_theta(theta, x[i]) - y[i])*x[i][j-1]
    return valeur / len(x)


def derivée_partielle_0( theta, x, y):
    valeur = 0
    for i in range(len(x)):
        valeur += (h_theta(theta, x[i]) - y[i])
    return valeur / len(x)


def etape_du_gradient(alpha, theta, x, y):
    n_theta = [theta[0] - alpha * derivée_partielle_0(theta, x, y)]
    for i,theta_i in enumerate(theta[1:]):
        n_theta.append(theta_i - alpha * derivée_partielle_par_rapport_à_theta_j(i+1, theta, x, y))
    return n_theta

def h_theta_b(theta, x_i):
    print("debut")
    print(x_i)
    print(theta[0])
    print(theta[1:])
    valeur = theta[0]
    for theta_j, x_i_j in zip(theta[1:], x_i):
        print(theta_j)
        print("exe")
        valeur += theta_j * x_i_j
    return valeur



tableau = sous_ensemble()
"""print(tableau)
theta = np.random.random((1, len(tableau[0])))[0]
print(theta)
x = np.array([x_i[:-1]for x_i in tableau])
y = np.array([y_i[-1] for y_i in tableau])
for i in range(100):
    print("cout", fonction_cout(theta, x, y))
    print("theta", theta)
    theta = etape_du_gradient(0.01, theta, x, y)
print("stop")
print(np.random.random((1, len(tableau[0]))))"""


def écart_relatif_en_pourcentage_entre_y_i_et_h_de_x_i_apres_descente_du_gradient(i,sous_ensemble):
    """
    fonction qui peut encore etre ameliorée mais est ce que ce srait vraiment utile d avoir les ecart relatifs?
    """
    ss_ensemble=list(sous_ensemble)
    x_i=ss_ensemble[i][:-1]
    y_i=ss_ensemble[i][-1]
    del ss_ensemble[i]
    theta = np.random.random((1, len(ss_ensemble[0])))[0]
    x=np.array(([x_j[:-1]for x_j in ss_ensemble]))
    y = np.array([y_i[-1] for y_i in ss_ensemble])
    for i in range(500):
        theta=etape_du_gradient(0.01, theta, x, y)
    return abs(y_i-h_theta(theta,x_i))/y_i*100

def moyenne_des_ecarts_relatifs(sous_ensemble):
    """
    fonction qui peut encore etre amelioree
    """
    ecart=0
    for i in range(len(sous_ensemble)):
        ecart+=écart_relatif_en_pourcentage_entre_y_i_et_h_de_x_i_apres_descente_du_gradient(i,sous_ensemble)
    return ecart/len(sous_ensemble)


def écart_absolu_entre_y_i_et_h_de_x_i_apres_descente_du_gradient(y,i,sous_ensemble):
    """
    :param y: numéro de la colonne du tableau extrait que l'on choisi pour etre le resultat (de 0 à len(sous_ensemble-1))
    :param i: numero de la ligne à laquelle on va appliquer h_theta apres descente du gradient pour comparer l'écart absolu entre cette valeur et y_i
    :param sous_ensemble: tableau extrait à partir duquel on veut travailler
    :return: écart absolu entre h_theta(x_i) et y_i apres descente du gradient
    """
    ss_ensemble=list(sous_ensemble)
    x_i=ss_ensemble[i][:y]+ss_ensemble[i][y+1:]
    y_i=ss_ensemble[i][y]
    del ss_ensemble[i]
    theta = np.random.random((1, len(ss_ensemble[0])))[0]
    x = np.array(([x_j[:y]+x_j[y+1:] for x_j in ss_ensemble]))
    y = np.array([y_j[y] for y_j in ss_ensemble])
    for i in range(500):
        theta=etape_du_gradient(0.01, theta, x, y)
    return abs(y_i-h_theta(theta,x_i))

def moyenne_des_ecarts_absolus(sous_ensemble):
    """
    :param sous_ensemble: tableau extrait sur lequel on veut travailler
    :return: moyenne de tous les ecarts absolus qu'on peut calculer dans ce tableau
    cette fonction est trop longue!!!! mais je l ai lancé et à la fin ça me donnait 0.24:en moyenne on predit une note à 0.24 près
    par contre le max c 3 et quelque je crois c assez enorme
    """
    ecart=0
    for y in range(len(sous_ensemble[0])):
        for i in range(len(sous_ensemble)):
            print(écart_absolu_entre_y_i_et_h_de_x_i_apres_descente_du_gradient(y,i,sous_ensemble))
            ecart+=écart_absolu_entre_y_i_et_h_de_x_i_apres_descente_du_gradient(y,i,sous_ensemble)
    return ecart/len(sous_ensemble)**2

print(moyenne_des_ecarts_absolus(tableau))