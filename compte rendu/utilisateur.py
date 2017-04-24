from movielens import Conversions, nombre_films
import math
import numpy as np


def grad_J_par_rapport_a_theta_i(Y, theta_i, i, X):
    y_i_tilde = Y.take(i, axis = 0)
    y_i_tilde = y_i_tilde.T
    l = []
    for i, y_i_k in enumerate(y_i_tilde):
        if not math.isnan(y_i_k):
            l.append(i)
    y_i_tilde = y_i_tilde.take(l, axis=0)
    X_tilde = X.take(l, axis=0)
    return np.dot(X_tilde.T, np.dot(X_tilde, theta_i.T) - y_i_tilde).T


def etape_du_gradient(Y, alpha_theta, theta, X):
    n_theta = []
    print(Y)
    for i, theta_i in enumerate(theta):
        n_theta.append(theta_i - alpha_theta * grad_J_par_rapport_a_theta_i(Y, theta_i, i, X))
    return np.array(n_theta)


class Utilisateur:
    """Une classe cense represente un utilisateur"""
    def __init__(self):
        """Initialise avec theta aleatoire"""
        self.films = {}
        self.conv = Conversions()
        self._theta = np.random.random((1, 50))

    def ajout_film(self, id_film, note):
        """Ajoute un film selon son id"""
        self.films[id_film] = note

    def theta(self, x, etapes):
        """Fait etapes etapes du gradient sur theta du film puis le renvoie"""
        y = np.array([[math.nan] * nombre_films()])
        for key in self.films:
            y[0][self.conv.renvoyer_index(key)] = self.films[key]
        for etape in range(etapes):
            self._theta = etape_du_gradient(y, 0.0001, self._theta, x)
        return self._theta

    def reccomandation(self, x):
        """"""
        y = np.array([[math.nan] * nombre_films()])
        for key in self.films:
            y[0][self.conv.renvoyer_index(key)] = self.films[key]
        max_i = 0
        n_max = 0
        t = np.dot(x, self._theta.T)
        print(t)
        for i, el in enumerate(y[0]):
            if np.isnan(el) and t[i, 0] > n_max:
                print("film : ", self.conv.renvoyer_nom_index(i), "note :", n_max)
                n_max = t[i, 0]
                max_i = i
        print(t)
        print(self._theta)
        return self.conv.renvoyer_nom_index(max_i)
