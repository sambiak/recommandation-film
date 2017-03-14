import numpy as np
from movielens import tableau_des_notes


def etape_gradient(α, l, x, θ, y):
    nu = len(y)
    nf = len(y[0])
    for i in range(nf):
        t = x[i]
        for k in range(l):
            t[k] = x[i][k] - α*sum([(θ[j].T @ x[i] - y[j][i]) * θ[j][k] for j in range(nu) if not np.isnan(y[j][i])])
        x[i] = t
    for j in range(nu):
        t = θ[j]
        for k in range(l):
            t[k] = θ[j][k] - α*sum([(θ[j].T @ x[i] - y[j][i]) * x[i][k] for i in range(nf) if not np.isnan(y[j][i])])
        θ[j] = t


α = 0.1
l = 10
y = tableau_des_notes()
nu = len(y)
nf = len(y[0])
x = np.random.random((nf, l))
θ = np.random.random((nu, l))
print(len(y[0]))
for i in range(10):
    etape_gradient(α, l, x, θ, y)
    print(θ[0])
    print(x[0])

