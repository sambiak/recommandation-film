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
    for i, theta_i in enumerate(theta):
        n_theta.append(theta_i - alpha_theta * grad_J_par_rapport_a_theta_i(Y, theta_i, i, X))
    return np.array(n_theta)


class Utilisateur:
    def __init__(self):
        self.films = {}
        self.conv = Conversions()
        self._theta = np.random.random((1, 10))

    def ajout_film(self, id_film, note):
        self.films[id_film] = note

    def theta(self, x, etapes):
        y = np.array([math.nan] * nombre_films())
        for key in self.films:
            y[self.conv.renvoyer_index(key)] = self.films[key]
        for etape in range(etapes):
            self._theta = etape_du_gradient(y, 0.1, self._theta, x)
        return self._theta

    def reccomandation(self, x):
        y = np.array([math.nan] * nombre_films())
        for key in self.films:
            y[self.conv.renvoyer_index(key)] = self.films[key]
        max_i = 0
        n_max = 0
        t = np.dot(x, self._theta.T)
        for i, el in enumerate(y):
            if el == math.nan and t[i] > n_max:
                n_max = t[i]
                max_i = i

        return self.conv.renvoyer_nom_index(max_i)
