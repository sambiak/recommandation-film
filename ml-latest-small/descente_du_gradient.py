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
    ecart=0
    for i in range(len(sous_ensemble)):
        ecart+=écart_relatif_en_pourcentage_entre_y_i_et_h_de_x_i_apres_descente_du_gradient(i,sous_ensemble)
    return ecart/len(sous_ensemble)


def écart_absolu_en_pourcentage_entre_y_i_et_h_de_x_i_apres_descente_du_gradient(i,sous_ensemble):
    ss_ensemble=list(sous_ensemble)
    x_i=ss_ensemble[i][:-1]
    y_i=ss_ensemble[i][-1]
    del ss_ensemble[i]
    theta = np.random.random((1, len(ss_ensemble[0])))[0]
    x=np.array(([x_j[:-1]for x_j in ss_ensemble]))
    y = np.array([y_i[-1] for y_i in ss_ensemble])
    for i in range(500):
        theta=etape_du_gradient(0.01, theta, x, y)
    return abs(y_i-h_theta(theta,x_i))

def moyenne_des_ecarts_absolus(sous_ensemble):
    ecart=0
    for i in range(len(sous_ensemble)):
        ecart+=écart_absolu_en_pourcentage_entre_y_i_et_h_de_x_i_apres_descente_du_gradient(i,sous_ensemble)
    return ecart/len(sous_ensemble)

print(moyenne_des_ecarts_absolus(tableau))