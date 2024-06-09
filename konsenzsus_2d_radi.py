import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def calculate_distances(r):
    n = len(r)
    desired_distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            desired_distances[i, j] = np.linalg.norm(r[i] - r[j])
            desired_distances[j, i] = desired_distances[i, j]
    
    return desired_distances


def konsenzus_protocol(r, tau, desired_distances, num_steps = 50):
    r_array = [r.copy()]

    
    step_size = 0.1

    for i in range(num_steps):
        r += step_size * tau

        r_array.append(r.copy())


    return r_array





if __name__ == "__main__":
    
    #gdje su inicijalno
    x = [1, 3, 3, 1]
    y = [3, 3, 1, 1]

    #tau - tj pomak, za koliko zelimo da se pomakne
    tau = np.array([2., 1.])

    #states
    r = np.array([[x[i], y[i]] for i in range(len(x))])
    r = r.astype(float)
    
    desired_distances = calculate_distances(r)

    num_steps = 50
    r_array = konsenzus_protocol(r, tau, desired_distances, num_steps=50)

    
    print(r_array)

    fig, ax = plt.subplots()
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_aspect('equal')
    ax.set_title('Trajectory of Agent Movement')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

    # Plot the trajectory of each agent
    lines = [ax.plot([], [], label=f'Agent {i+1}')[0] for i in range(len(r))]

    # Update function for animation
    def update(frame):
        for i, line in enumerate(lines):
            line.set_data([pos[i, 0] for pos in r_array[:frame+1]], [pos[i, 1] for pos in r_array[:frame+1]])
        return lines

    # Animation
    ani = FuncAnimation(fig, update, frames=num_steps+1, interval=200, blit=True)
    plt.legend()
    plt.show()

    
    
    