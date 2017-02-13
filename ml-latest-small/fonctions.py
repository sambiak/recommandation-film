from movielens import sous_ensemble
import numpy as np
import math
def moyenne_des_notes_des_film(array):
    """renvoit la liste des moyennes des notes par film en prenant le tableau des notes"""
    list_moy = []
    k=0
    moy=0
    for i in range(9125):
        for j in (array[:,i]):
            if not math.isnan(j) :
                k+=1
                moy+=j
        if k==0:
            list_moy += [math.nan]
        else:
            list_moy += [moy/k]
    return list_moy


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


def derivée_partielle(theta_i, theta, x, y):
    valeur = 0
    for i in range(len(x)):
        valeur += (h_theta(theta, x[i]) - y[i])
    return valeur * theta_i / len(x)


def derivée_partielle_0( theta, x, y):
    valeur = 0
    for i in range(len(x)):
        valeur += (h_theta(theta, x[i]) - y[i])
    return valeur / len(x)


def etape_du_gradient(alpha, theta, x, y):
    n_theta = [theta[0] - alpha * derivée_partielle_0(theta, x, y)]
    for theta_i in theta[1:]:
        n_theta.append(theta_i - alpha * derivée_partielle(theta_i, theta, x, y))
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
print(tableau)
theta = np.random.random((1, len(tableau[0])))[0]
print(theta)
x = np.array([x_i[:-1]for x_i in tableau])
y = np.array([t[-1] for t in tableau])
for i in range(100):
    print("cout", fonction_cout(theta, x, y))
    print("theta", theta)
    theta = etape_du_gradient(0.01, theta, x, y)
print("stop")
print(np.random.random((1, len(tableau[0]))))

