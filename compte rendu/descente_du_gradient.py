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


def derivee_partielle_par_rapport_a_theta_j(j, theta, x, y):
    valeur = 0
    for i in range(len(x)):
        valeur += (h_theta(theta, x[i]) - y[i])*x[i][j-1]
    return valeur / len(x)


def derivee_partielle_0( theta, x, y):
    valeur = 0
    for i in range(len(x)):
        valeur += (h_theta(theta, x[i]) - y[i])
    return valeur / len(x)


def etape_du_gradient(alpha, theta, x, y):
    n_theta = [theta[0] - alpha * derivee_partielle_0(theta, x, y)]
    for i,theta_i in enumerate(theta[1:]):
        n_theta.append(theta_i - alpha * derivee_partielle_par_rapport_a_theta_j(i+1, theta, x, y))
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

def ecart_absolu_entre_y_i_et_h_de_x_i_apres_descente_du_gradient(y,i,sous_ensemble):
    """
    :param y: numero de la colonne du tableau extrait que l'on choisi pour etre le resultat
    (de 0 a len(sous_ensemble)-1)
    :param i: numero de la ligne a laquelle on va appliquer h_theta apres descente du
    gradient pour comparer l'ecart absolu entre cette valeur et y_i
    :param sous_ensemble: tableau extrait a partir duquel on veut travailler
    :return: ecart absolu entre h_theta(x_i) et y_i apres descente du gradient
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
    cette fonction est trop longue!!!! mais je l ai lance et a la fin ca me donnait 0.24 : en
    moyenne on predit une note a 0.24 pres
    par contre le max c 3 et quelque je crois c assez enorme
    """
    ecart=0
    for y in range(len(sous_ensemble[0])):
        for i in range(len(sous_ensemble)):
            print(ecart_absolu_entre_y_i_et_h_de_x_i_apres_descente_du_gradient\
                      (y,i,sous_ensemble))
            ecart+=ecart_absolu_entre_y_i_et_h_de_x_i_apres_descente_du_gradient\
                (y,i,sous_ensemble)
    return ecart/len(sous_ensemble)**2

if __name__ == "__main__":
    tableau = sous_ensemble()
    print(moyenne_des_ecarts_absolus(tableau))
