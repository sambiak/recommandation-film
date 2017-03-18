import numpy as np
import math
from movielens import tableau_des_notes


def sorte_de_fonction_cout(Y, theta, X):
    valeur = 0
    c = 0
    for i in range (len(Y)):
        for j in range (len(Y[0])):
            if not math.isnan(Y[i, j]):
                c+=1
                valeur += abs(np.dot(theta[j].T, X[i])-Y[i, j])
    return valeur/c


def grad_J_par_rapport_a_theta_j(Y, theta_j, j, X):
    y_j_tilde = Y.take(j, axis = 1)
    l = []
    for i, y_j_k in enumerate(y_j_tilde):
        if not math.isnan(y_j_k):
            l.append(i)
    y_j_tilde = y_j_tilde.take(l, axis=0)
    X_tilde = X.take(l, axis=0)
    return np.dot(X_tilde.T, np.dot(X_tilde, theta_j.T) - y_j_tilde).T


def grad_J_par_rapport_a_x_i(Y, x_i, i, theta):
    y_i_tilde = Y.take(i, axis = 0)
    y_i_tilde = y_i_tilde.T
    l = []
    for i, y_i_k in enumerate(y_i_tilde):
        if not math.isnan(y_i_k):
            l.append(i)
    y_i_tilde = y_i_tilde.take(l, axis=0)
    theta_tilde = theta.take(l, axis=0)
    return np.dot(theta_tilde.T, np.dot(theta_tilde, x_i.T) - y_i_tilde).T


def etape_du_gradient(Y, alpha, theta, X):

    n_theta = []
    for j, theta_j in enumerate(theta):
        n_theta.append(theta_j - alpha * grad_J_par_rapport_a_theta_j(Y, theta_j, j, X))

    n_X = []
    for i, x_i in enumerate(X):
        n_X.append(x_i - alpha * grad_J_par_rapport_a_x_i(Y, x_i, i, theta))

    return np.array(n_theta), np.array(n_X)


def descente_du_gradient(Y, l, nb_etapes, alpha):
    #ça serait surement plus efficace de prendre deux alpha differents pour X et theta
    theta = np.random.random((len(Y[0]), l))
    X = np.random.random((len(Y), l))
    for etape in range (nb_etapes):
        theta, X = etape_du_gradient(Y, alpha, theta, X)
        print(etape)
        #print(np.dot(theta[0], x[30]))
        print(sorte_de_fonction_cout(Y, theta, X))
    return theta, X


Y=tableau_des_notes()

descente_du_gradient(Y, 10, 500, 0.0001)
