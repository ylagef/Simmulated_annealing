import random

import matplotlib.pyplot as plt
import numpy as np


def simulated_annealing(init_x, neighborhood, init_temp, temp_variation, iterations, graphs):
    def f(x):
        # f(x)=sin(0.15*x)+cos(x)
        # 0 <= x <= 40
        return np.sin(0.15 * x) + np.cos(x)

    def neighbor_acceptance(x):  # Calculates the neighbor value and decide if accept it or not
        r_acceptance = random.random()  # Random value behind 0 and 1 for acceptance

        left = x - (x * neighborhood)  # Alpha percent of left
        right = x + ((40 - x) * neighborhood)  # Alpha percent of right

        neighbor_x = random.uniform(left, right)  # Random value behind neighborhood range

        cost = abs(f(neighbor_x) - f(x))  # Cost. Abs of difference between energies

        if f(neighbor_x) > f(x):  # Accept new value (it's better)
            return [1, neighbor_x]
        elif np.exp(-cost / temp) > r_acceptance:  # Random accepting worst new value
            return [1, neighbor_x]
        else:
            return [0, x]  # Not accepted new value

    def print_graphs():
        plt.figure(1)

        # Print temp graph
        plt.subplot(211)
        plt.title("Temperature")
        plt.ylabel("Temp (ºK)")
        plt.xlabel("Iteration")
        plt.plot(temp_graph, 'r', linewidth=0.5)
        plt.grid(True)

        # Print f(x) and x with steps
        t1 = np.arange(0.0, 40.0, 0.1)
        plt.subplot(212)
        plt.title("f(x)=sin(0.15*x)+cos(x)")
        plt.ylabel("f(x)")
        plt.xlabel("x")
        for l, m in steps.items():
            plt.plot(t1, f(t1), 'b', m, f(m), 'rx', linewidth=0.5)
        plt.grid(True)

        plt.show()

    steps = dict()  # Movements to achieve optimization
    step_iteration = 0
    temp_graph = []

    # Initialize values and do iterations
    x_value = init_x
    temp = init_temp
    for i in range(iterations):  # Iterations for optimization

        n_acceptance = neighbor_acceptance(x_value)
        accepted = n_acceptance[0]
        new_x = n_acceptance[1]

        if accepted:
            x_value = new_x
            steps[step_iteration] = x_value
            step_iteration = step_iteration + 1

        temp = temp * temp_variation
        temp_graph.append(temp)

    # Calculates final max and its iteration
    maximum = 0
    iteration = 0
    for k, v in steps.items():
        if f(v) > f(maximum):
            maximum = v
            iteration = k

    # Print the results and used parameters
    print("\nFINAL RESULT:\nMaximum value", f(maximum), "at x =", maximum, "- Iteration", iteration, "/",
          (iterations - 1))
    print("Parameters:\n\tInitial x value =", init_x, "\n\tAlpha (neighborhood) =", neighborhood,
          "\n\tStart temperature =", init_temp, "\n\tBeta (Temp variation) =", temp_variation, "\n\tIterations =",
          iterations)

    if graphs:
        print_graphs()


init_x = 0  # Initial X value
neighborhood = 0.5  # Alpha
init_temp = 100  # Start temperature
temp_variation = 0.99  # Beta
iterations = 10000  # Number of iterations

simulated_annealing(init_x, neighborhood, init_temp, temp_variation, iterations, 0)
