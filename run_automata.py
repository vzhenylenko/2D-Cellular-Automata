# Author: Viacheslav Zhenylenko
# TODO: Clean, complete unfinised parts, add comments

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.animation import FuncAnimation
import random
from math import sqrt
import sys, getopt
from config import *

def get_rectangular_positions(n):
    positions = np.zeros(n, dtype=[('position', float, 2)])
    positions = positions['position']
    x = np.linspace(0, 1, int(sqrt(n))) + 0.02
    i = 0
    for xi in x:
        for xj in x:
            if i < n:
                positions[i] = (xj, xi)
                i += 1
    return positions

# TODO
def get_triangular_positions(n):
    positions = np.zeros(n, dtype=[('position', float, 2)])
    positions = positions['position']
    x = np.linspace(0, 1, int(sqrt(n))) + 0.02
    i = 0
    for xi in x:
        for xj in x:
            if i < n:
                positions[i] = (xj, xi)
                i += 1
    return positions

# TODO
def get_hexagonal_positions(n):
    positions = np.zeros(n, dtype=[('position', float, 2)])
    positions = positions['position']
    x = np.linspace(0, 1, int(sqrt(n))) + 0.02
    i = 0
    for xi in x:
        for xj in x:
            if i < n:
                positions[i] = (xj, xi)
                i += 1
    return positions

class Cell:

    def __init__(self):
        self.is_alive = False
        self.neighbours_list = []


def initialize_rectangular_cells(n, neighbours_type):
    cells = []
    side = int(sqrt(n))
    for i in range(side):
        for j in range(side):
            m = i * side + j
            cell = Cell()

            if neighbours_type == 'rect_four':
                mask = [i != 0, i != side - 1,  j != 0, j != side - 1]
                values = [m - side, m + side, m - 1, m + 1]

            elif neighbours_type == 'rect_eight':
                mask = [i != 0, i != side - 1, j != 0, j != side - 1,
                        i != 0 and j != 0, i != side - 1 and j != side - 1,
                        i != 0 and j != side - 1, i != side - 1 and j != 0]
                values = [m - side, m + side, m - 1, m + 1,
                          m - 1 - side, m + 1 + side,
                          m + 1 - side, m - 1 + side]

            for include, index in zip(mask, values):
                if include:
                    cell.neighbours_list.append(index)
            cells.append(cell)

    if WRAP_TYPE == 'cylinder':
        if neighbours_type == 'rect_four':
            for i in range(side):
                cells[i * side].neighbours_list.append((i + 1) * side - 1)
                cells[(i + 1) * side - 1].neighbours_list.append(i * side - 1)
        elif neighbours_type == 'rect_eight':
            for i in range(side):
                cells[i * side].neighbours_list.append((i + 1) * side - 1)
                cells[(i + 1) * side - 1].neighbours_list.append(i * side - 1)
                # TODO: add other

    elif WRAP_TYPE == 'meobius':
        if neighbours_type == 'rect_four':
            for i in range(side):
                cells[i * side].neighbours_list.append((i + 1) * side - 1)
                cells[(i + 1) * side - 1].neighbours_list.append(
                    i * side - 1)
            for j in range(side):
                cells[(side - 1) * side + j].neighbours_list.append(j)
                cells[j].neighbours_list.append((side - 1) * side + j)

        if neighbours_type == 'rect_four':
            for i in range(side):
                cells[i * side].neighbours_list.append((i + 1) * side - 1)
                cells[(i + 1) * side - 1].neighbours_list.append(
                    i * side - 1)
            for j in range(side):
                cells[(side - 1) * side + j].neighbours_list.append(j)
                cells[j].neighbours_list.append((side - 1) * side + j)
                # TODO: add corners

    if IS_RANDOM:
        is_alive_list = [True if random.uniform(0, 1) <= PROB else False for i in range(n)]
    else:
        is_alive_list = [False] * N

    #random.choice([True, False])
    #is_alive_list = [False] * n

    return cells, is_alive_list

# TODO
def initialize_triangular_cells(n, neighbours_type):
    pass

# TODO
def initialize_hexagonal_cells(n, neighbours_type):
    pass

def initialize_center(cells, is_alive_list, layout_id):

    center_cells = LAYOUT_DICT[layout_id]
    k = 5
    side = int(sqrt(N))
    i, j = int(side / 2) + k, int(side / 2) + k
    m = i * side + j

    for col_delta in range(len(center_cells)):
        for row_delta in range(len(center_cells[col_delta])):
            ind = m - side * row_delta + col_delta
            if center_cells[col_delta][row_delta]:
                cells[ind].is_alive = True
                is_alive_list[ind] = True

def update_algo_1(i, neighs, is_alive_list):
    count = 0
    for i in neighs:
        if is_alive_list[i]:
            count += 1

    if count in COUNT_LIST:
        return True
    else:
        return False

def update_algo_2(i, neighs, is_alive_list):
    count = 0
    for j in neighs:
        if is_alive_list[j]:
            count += 1

    if count == 3:
        return True
    elif count == 2:
        return is_alive_list[i]
    else:
        return False

def update_cells(cells, is_alive_list, update_algo):
    l = len(cells)
    is_alive_new = [False] * l

    for i, cell in enumerate(cells):
        neighs = cell.neighbours_list
        is_alive_new[i] = update_algo(i, neighs, is_alive_list)

    for i, cell in enumerate(cells):
        cell.is_alive = is_alive_new[i]

    return is_alive_new

def update_plot(frame_number):
    global cells, is_alive_list
    if frame_number != 0:
        is_alive_list = update_cells(cells, is_alive_list, update_algos[UPDATE_ALGORITHM])
        for i in range(N):
            col = COL_LIVE if is_alive_list[i] == True else COL_DEAD
            #col = random.choice([(1, 0, 0, 1), (0, 1, 0, 1)])
            dots['color'][i] = col
    # Update the scatter collection with new colors.
    scat.set_facecolors(dots['color'])


def simulation():
    global is_alive_list
    i = 0
    densities = []
    densities.append(is_alive_list.count(True) / len(is_alive_list))

    while i < ITERATIONS:
        is_alive_list = update_cells(cells, is_alive_list, update_algos[UPDATE_ALGORITHM])
        densities.append(is_alive_list.count(True) / len(is_alive_list))
        i += 1
        if i % 100 == 0:
            print(i)

    densities = pd.Series(densities)
    print(densities[40:].mean())
    #print(densities)

    k2, p = stats.normaltest(densities[40:])
    alpha = 1e-3
    print("p = {:g}".format(p))
    if p < alpha:  # null hypothesis: x comes from a normal distribution
        print("The null hypothesis can be rejected")
    else:
        print("The null hypothesis cannot be rejected")

    densities.hist(bins=50)
    return densities

#if __name__ == "__main__":

init_func_dict = {'rectangular': initialize_rectangular_cells,
                  'triangular': initialize_triangular_cells,
                  'hexagonal': initialize_hexagonal_cells}

update_algos = {'life regular': update_algo_2,
                'life custom': update_algo_1}

''' 0. PLOT ENVIRONMENT INITIALIZATION '''
np.random.seed(19680801)
fig = plt.figure(figsize=FIGSIZE)
ax = fig.add_axes([0, 0, 1, 1], frameon=False)

''' 1. CELLS INITIALIZATION '''
cells, is_alive_list = init_func_dict[LAYOUT_TYPE](N, NEIGHBOURS_TYPE)
if INITIAL_SETUP:
    initialize_center(cells, is_alive_list, LAYOUT_ID)

densities = []

if MAKE_PLOT:
    dots = np.zeros(N, dtype=[('position', float, 2), ('size', float, 1), ('color', float, 4)])
    dots['position'] = get_rectangular_positions(N)
    for i in range(N):
        color = COL_LIVE if is_alive_list[i] == True else COL_DEAD
        dots['color'][i] = color
        dots['size'][i] = 20

    ax.set_xlim(0, 1.05), ax.set_xticks([])
    ax.set_ylim(0, 1.05), ax.set_yticks([])

    scat = ax.scatter(dots['position'][:, 0], dots['position'][:, 1],
                      s=dots['size'], lw=0.5,
                      facecolors=dots['color'])
    animation = FuncAnimation(fig, update_plot, interval=int(1000 / SPEED))
    plt.show()

elif MAKE_SIMULATION:
    global PROB
    probs = []
    for i in range(10, 12):
        curr = []
        for j in range(3):
            PROB = i
            sim = simulation()
            curr.append(sim[40:].mean())
            #print(sim[100:].mean())
        #if sum(curr) / 10 > 0.6:
        #    curr =
        #probs.append()

    print(probs)
    #plt.plot(probs)
    plt.show()
