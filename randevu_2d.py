#radim sa 2 dimenzije
#sto je stopping uvijet?

import numpy as np
import matplotlib.pyplot as plt

#za plottanje dok se micu
def moving_plot(r_array):
    plt.figure()

    plt.xlim(0, 5)
    plt.ylim(0, 5)
    for r in r_array:
        plt.scatter(r[:, 0], r[:, 1], c = "r")
        plt.pause(1)


    
    plt.legend()
    plt.show()

#za plottanje u 2D
def plot_me(r):

    x = r[:, 0]
    y = r[:, 1]
    plt.figure()
    plt.scatter(x, y, c='r', marker='o')

    plt.xlim(0, 5)
    plt.ylim(0, 5)


    plt.grid(True)
    plt.show()


def update_r(r, dr, dt):
    #dr -> brzina v
    #v = s/t  -> s = v*t = dr * dt
    #dt je step size
    #a dr je - aij * (rj - ri)
    r = r + dr * dt
    return r

def calculate_dr(a, r, control_gain=0.1):
    dr =  np.zeros_like(r)
    
    n = len(r)
    for i in range(n):
        dr_elem = [0, 0]
        for j in range(n):
            dr_elem += a[i][j] * (r[j] - r[i])
            
        dr[i] = dr_elem * control_gain
        

    return dr


#gleda kad je uvijet randevua zadovoljen
def uvijet_prekidanja(a, r, tresh = 0.2):
    n = len(r)
    for i in range(n):
        
        for j in range(n):
            if a[i][j] == 0:
                continue
            udaljenost = np.linalg.norm(r[j] - r[i]) 
            if udaljenost >= tresh:
                return False
    
    
    return True


def consensus_protocol(x, y, r, adjacency_matrix ):
    n = len(x)
    
    #matrica za komuniciranje, želiimo da se sve sudare
    
    print(adjacency_matrix)
    #plot_me(x, y)

    nasli_se = False

    iter = 0

    # t -> oo
    dt = 0.1
    control_gain = 0.5

    

    r_list = [r]
    while nasli_se == False:
        iter = iter + 1

        dr = calculate_dr(adjacency_matrix, r, control_gain)
        r = update_r(r, dr, dt)
        
        r_list.append(r)
        
        
        nasli_se = uvijet_prekidanja(adjacency_matrix, r)
        


    
    moving_plot(r_list)
    print(iter)






if __name__ == "__main__":
    

    x = [1, 3, 3, 1]
    y = [3, 3, 1, 1]

    #states
    r = np.array([[x[i], y[i]] for i in range(len(x))])
    r = r.astype(float)
     
    n = len(x)

    #matrica da se sva 4 sudare jednakom brzinom(?) - koreografija  1 iz prezentacije
    adjacency_matrix = np.ones((n, n)) - np.eye(n)

    #koregorFIJA 2 iz prezentacije
    #adjacency_matrix = np.array([[0, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
    

    #zelimo da se sudare prva i druga  i    treca i cetvrta - koreografija 3 iz prezentacije
    #adjacency_matrix = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]])

    #koreo 5 
    #adjacency_matrix = np.array([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]])

    #koreo 6
    #adjacency_matrix = np.array([[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0]])

    #koreo 4
    #adjacency_matrix = np.array([[0, 1, 0, 1], [0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0]])

    #zelimo da se neke micu brze 
    #adjacency_matrix = np.array([[0, 2, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 2, 0]])
    consensus_protocol(x, y, r, adjacency_matrix)