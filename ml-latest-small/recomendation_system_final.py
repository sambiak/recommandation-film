import numpy as np
import math
from movielens import tableau_des_notes, tableau_bricolé_de_l_lignes_et_c_colonnes


def fonction_cout(Y, theta, X):
    """
    :param Y: tableau de notes avec utilisateurs en lignes et films en colonnes
    :param theta: tableau avec des lignes de profils d'utilisateurs
    :param X: tableau avec des lignes de caracteristiques de films
    :return: valeur la fonction de cout en theta et X
    """
    return np.nanmean((np.dot(X, theta.T) - Y.T) ** 2)


def grad_J_par_rapport_a_x_j(Y, x_j, j, theta):
    """
    :param Y: tableau de notes avec utilisateurs en lignes et films en colonnes
    :param x_j: ligne j de X par rapport à laquelle nous calculons les derivees partielles de la fonction de cout
                (correspond aux caracteristiques du film j)
    :param j: numero de la ligne de X par rapport à laquelle nous calculons les derivees partielles de la fonction de cout
    :param theta: tableau avec des lignes de profils d'utilisateurs
    :return: valeur du gradient de la fonction de cout prise en theta et X par rapport a x_j
    """
    y_j_tilde = Y.take(j, axis = 1)
    y_j_tilde, theta_tilde = y_j_tilde[~np.isnan(y_j_tilde)], theta[~np.isnan(y_j_tilde)]
    return np.dot(theta_tilde.T, np.dot(theta_tilde, x_j.T) - y_j_tilde).T


def grad_J_par_rapport_a_theta_i(Y, theta_i, i, X):
    """
    :param Y: tableau de notes avec utilisateurs en lignes et films en colonnes
    :param theta_i: ligne i de theta par rapport à laquelle nous calculons les derivees partielles de la fonction de cout
            (correspond aux caracteristiques du film j)
    :param i: numero de la ligne de theta par rapport à laquelle nous calculons les derivees partielles de la fonction de cout
    :param X: theta: tableau avec des lignes de profils d'utilisateurs
    :return: valeur du gradient de la fonction de cout prise en theta et X par rapport a theta_i
    """
    y_i_tilde = Y.take(i, axis = 0)
    y_i_tilde = y_i_tilde.T
    y_i_tilde, X_tilde = y_i_tilde[~np.isnan(y_i_tilde)], X[~np.isnan(y_i_tilde)]
    return np.dot(X_tilde.T, np.dot(X_tilde, theta_i.T) - y_i_tilde).T


def etape_du_gradient(Y, alpha_X, alpha_theta, theta, X):
    """
    :param Y: tableau de notes avec utilisateurs en lignes et films en colonnes
    :param alpha_X: taux d apprentissage pour la modification de X
    :param alpha_theta: taux d apprentissage pour la modification de theta
    :param theta: tableau avec des lignes de profils d'utilisateurs
    :param X: tableau avec des lignes de caracteristiques de films
    :return: theta et X modifiés apres une etape de descente du gradient
    """

    n_X = [0] * len(X)
    for j, x_j in enumerate(X):
        n_X[j] = (x_j - alpha_X * grad_J_par_rapport_a_x_j(Y, x_j, j, theta))

    n_theta = [0] * len(theta)
    for i, theta_i in enumerate(theta):
        n_theta[i] = (theta_i - alpha_theta * grad_J_par_rapport_a_theta_i(Y, theta_i, i, X))

    return np.array(n_theta), np.array(n_X)


def descente_du_gradient(Y, nb_carac, nb_etapes, alpha_X, alpha_theta):
    """
    :param Y: tableau de notes avec utilisateurs en lignes et films en colonnes
    :param nb_carac: nombre de caracteristiques de films (nb de colonnes de theta et X)
    :param nb_etapes: nb d etapes de descente du gradient à realiser
    :param alpha_X: taux d apprentissage pour la modification de X avec la descente du gradient
    :param alpha_theta: taux d apprentissage pour la modification de theta avec la descente du gradient
    :return: theta et X modifiés après nb_etapes d'étapes de descente du gradient
    """
    X = np.random.random((len(Y[0]), nb_carac))
    theta = np.random.random((len(Y), nb_carac))
    for etape in range(nb_etapes):
        theta, X = etape_du_gradient(Y, alpha_X, alpha_theta, theta, X)
        print("etape", etape)
    return theta, X

if __name__ == "__main__":
    Y=tableau_des_notes()
    descente_du_gradient(Y, 10, 100, 0.001, 0.0001)

