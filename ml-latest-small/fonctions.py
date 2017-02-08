from movielens import *
def moyenne_des_notes_des_film(fonction):
    """renvoit la liste des moyennes des notes par film en prenant le tableau des notes"""
    moy = 0
    list_moy = []
    k = 0
    for i in range(9125):
        for j in fonction:
            if not math.isnan(float(j[i])):            
                moy += j[i]
                k += 1
        if k != 0:
            moy = moy / k
        else:
            moy = float('nan')
        list_moy += [moy]
    return list_moy

print(moyenne_des_notes_par_film(tableau_des_notes()))

