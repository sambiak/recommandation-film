import numpy as np
import math
from movielens import tableau_des_notes, tableau_bricolé_de_l_lignes_et_c_colonnes


def sorte_de_fonction_cout(Y, theta, X):
    valeur = 0
    c = 0
    for i in range (len(Y)):
        for j in range (len(Y[0])):
            if not math.isnan(Y[i, j]):
                c+=1
                valeur += abs(np.dot(X[j], theta[i].T)-Y[i, j])
    return valeur/c


def grad_J_par_rapport_a_x_j(Y, x_j, j, theta):
    y_j_tilde = Y.take(j, axis = 1)
    y_j_tilde, theta_tilde = y_j_tilde[~np.isnan(y_j_tilde)], theta[~np.isnan(y_j_tilde)]
    return np.dot(theta_tilde.T, np.dot(theta_tilde, x_j.T) - y_j_tilde).T


def grad_J_par_rapport_a_theta_i(Y, theta_i, i, X):
    y_i_tilde = Y.take(i, axis = 0)
    y_i_tilde = y_i_tilde.T
    y_i_tilde, X_tilde = y_i_tilde[~np.isnan(y_i_tilde)], X[~np.isnan(y_i_tilde)]
    return np.dot(X_tilde.T, np.dot(X_tilde, theta_i.T) - y_i_tilde).T


def etape_du_gradient(Y, alpha_X, alpha_theta, theta, X):

    n_X = []
    for j, x_j in enumerate(X):
        n_X.append(x_j - alpha_X * grad_J_par_rapport_a_x_j(Y, x_j, j, theta))

    n_theta = []
    for i, theta_i in enumerate(theta):
        n_theta.append(theta_i - alpha_theta * grad_J_par_rapport_a_theta_i(Y, theta_i, i, X))

    return np.array(n_theta), np.array(n_X)


def descente_du_gradient(Y, l, nb_etapes, alpha_X, alpha_theta):
    X = np.random.random((len(Y[0]), l))
    theta = np.random.random((len(Y), l))
    for etape in range(nb_etapes):
        theta, X = etape_du_gradient(Y, alpha_X, alpha_theta, theta, X)
        print("etape", etape)
        print(sorte_de_fonction_cout(Y, theta, X))
    return theta, X

if __name__ == "__main__":
    Y=tableau_des_notes()
    descente_du_gradient(Y, 10, 500, 0.001, 0.0001)


"""
#tableau que j ai extrait en prenant 5 utilisateurs qui ont notés ou pas dans l ordre :
#forrest gump (war,romance,comedy,drama), gost buster (action, comedy, sf), star wars (action aventure sf)
#et jurassic park (action aventure sf thriller)
# c galere a analyser en fait sur un tt petit tableau il sort pas forcement des trucs logiques qui sautent aux yeux

Y = tableau_bricolé_de_l_lignes_et_c_colonnes(tableau_des_notes(), 30, 14)[0].take([0,1,4,6], axis = 1).take([10, 11, 13, 20, 23], axis = 0)
theta, X = descente_du_gradient(Y, 5, 20000, 0.0001, 0.001)
print(theta)
print(" ")
print(X)
"""

"""
#tableau du mooc : notre programme separe bien l'action de la romance

na_n = float('nan')
Y = np.array([[5,5,0,0],[5,na_n,na_n,0],[na_n,4,0,na_n],[0,0,5,4],[0,0,5,na_n]]).T
theta, X = descente_du_gradient(Y, 2, 10000, 0.0001, 0.001)
print(theta)
print(" ")
print(X)
"""

print(np.isnan(tableau_des_notes()).sum())