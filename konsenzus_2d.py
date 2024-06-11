
import numpy as np
import matplotlib.pyplot as plt

#slajd 26

#za plottanje dok se micu
def moving_plot(r_array):
    plt.figure()

    

    plt.xlim(0, 10)
    plt.ylim(0, 10)
   
    
    plt.grid(True)

    zadnji = len(r_array)
    
    iter = 0
    for r in r_array:
        if iter == 0:
            plt.scatter(r[:, 0], r[:, 1], c="b")
            iter = iter + 1
            continue
        if iter == zadnji - 1:
            plt.scatter(r[:, 0], r[:, 1], c="g")
            
            continue
        iter = iter + 1
        plt.scatter(r[:, 0], r[:, 1], c="r")
        plt.pause(1)


    
    plt.legend()
    plt.show()
    return

#za plottanje u 2D
def plot_me(r):

    x = r[:, 0]
    y = r[:, 1]
    plt.figure()
    plt.scatter(x, y, marker='o')

    plt.xlim(0, 5)
    plt.ylim(0, 5)


    plt.grid(True)
    plt.show()




def calculate_dx(a, x, ksi, y = 1.0):
    dx =  np.zeros_like(x)
    
    n = len(x)
    
    for i in range(n):
        #print("SADA RADIMO ZA LETJELICU {}".format(i))
        dr_elem = [0, 0]
        
        for j in range(n):
            dr_elem +=  a[i][j]  * ((x[j] - x[i]) - (ksi[j] - ksi[i]))
            #print("x:")
            #print((x[j] - x[i]))
            #print("ksi")
            #print((ksi[j] - ksi[i]))
 
        #print(dr_elem)
        dx[i] = dr_elem * y
        #print("-----------------------------------------------------")

    #print("DERIVACIJA JE: ")
    #print(dx)
    return dx





def consensus_protocol(x, ksi, adjacency_matrix ):
    n = len(x)
    print(n)
   
    print(adjacency_matrix)
    
    iter = 0

    # t -> oo
    dt = 0.05 #0.05
    

    
    
    x_list = [x.copy()]
    while True:
   
        iter = iter + 1
        
        
        
        dx = calculate_dx(adjacency_matrix, x, ksi)
        x = x + dx * dt
        

        #print("UPDEJTATI X JE")
        #print(x)
        
        x_list.append(x.copy())
        
        
        
        #nasli_se = uvijet_prekidanja(adjacency_matrix, r)
        if iter == 10:
            break
        


    print(x_list[8])
    moving_plot(x_list)
    print(iter)






if __name__ == "__main__":
    

    x = [4.,  6.,8.]
    y = [4., 7.,  4.]

    ksi_x = [4.2, 6.2, 8.3]
    ksi_y = [4.2, 6.8, 3.5]

    

    #states - početna formacija
    x = np.array([[x[i], y[i]] for i in range(len(x))])
    x = x.astype(float)

    

    ksi = np.array([[ksi_x[i], ksi_y[i]] for i in range(len(x))])
    ksi = ksi.astype(float)
    
   
    
    n = len(x)
    print(x)
    print(ksi)
    print("=============================")

    #matrica da se sva 4 sudare jednakom brzinom(?) - koreografija  1 iz prezentacije
    adjacency_matrix = np.ones((n, n)) - np.eye(n)
    
    
    consensus_protocol(x, ksi , adjacency_matrix)