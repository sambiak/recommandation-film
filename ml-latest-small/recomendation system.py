import numpy as np
import math
from movielens import tableau_des_notes

def theta_j_transpose_x_i(theta, j, x, i):
    """
    :param theta: array numpy qui est en fait une liste des theta (sans theta_i_0) pour chaque utilisateur
    :param j: numero du theta concerné, theta de l'utilisteur n°j
    :param x: array numpy qui est une liste des features pour chaque film
    :param i: numero du x concerné, features du film n°i
    :return: theta_j_transpose_x_i
    """

    return np.dot(theta[j].T, x[i])

def fonction_cout(y, theta, x):
    valeur = 0
    c = 0
    for i in range (len(y)):
        for j in range (len(y[0])):
            if not math.isnan(y[i,j]):
                c+=1
                valeur += np.dot(theta[j].T, x[i])-y[i,j]
    return valeur/c


def dérivée_partielle_par_rapport_à_theta_j_k(y, theta_j, j, k, x):
    valeur = 0
    for i in range(len(x)):
        if not math.isnan(y[i,j]):
            valeur += (np.dot(theta_j.T, x[i]) - y[i,j]) * x[i,k]
    return valeur


def dérivée_partielle_par_rapport_à_x_i_k(y, x_i, i, k, theta):
    valeur = 0
    for j in range(len(theta)):
        if not math.isnan(y[i, j]):
            valeur += (np.dot(theta[j].T, x_i) - y[i, j]) * theta[j, k]
    return valeur


def etape_du_gradient(y, alpha, theta, x):

    n_theta = []
    for j,theta_j in enumerate(theta):
        n_theta_j=[]
        for k, theta_j_k in enumerate(theta_j):
            n_theta_j.append(theta_j_k - alpha * dérivée_partielle_par_rapport_à_theta_j_k(y, theta_j, j, k, x))
        n_theta.append(n_theta_j)

    n_x = []
    for i, x_i in enumerate(x):
        n_x_i = []
        for k, x_i_k in enumerate(x_i):
            n_x_i.append(x_i_k - alpha * dérivée_partielle_par_rapport_à_x_i_k(y, x_i, i, k, theta))
        n_x.append(n_x_i)

    return np.array(n_theta), np.array(n_x)

def descente_du_gradient(y, l, nb_etapes, alpha):
    theta = np.random.random((len(y[0]), l))
    x = np.random.random((len(y), l))
    for etape in range (nb_etapes):
        theta, x = etape_du_gradient(y, alpha, theta, x)
        print(etape)
        print(np.dot(theta[0], x[30]))
        print(fonction_cout(y, theta, x))
    return theta, x

y=tableau_des_notes()
y[0,30]= float('nan')

theta, x = descente_du_gradient(y, 10, 100, 0.0001)

