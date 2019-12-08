#from run_automata import initialize_rectangular_cells

N = 10000

COL_LIVE = (0, 1, 0, 1)
COL_DEAD = (0.6, 0.6, 0.6, 1)
COL_DEAD = (1, 0, 0, 1)

MAKE_PLOT = True
#MAKE_PLOT = False
MAKE_SIMULATION = True
ITERATIONS = 150

SPEED = 100

LAYOUT_TYPE = 'rectangular'
NEIGHBOURS_TYPE = 'rect_four' # 'rect_eight', 'hexagonal'
#NEIGHBOURS_TYPE = 'rect_eight'
WRAP_TYPE = 'bounded' # 'cylinder', 'moebius'
#WRAP_TYPE = 'cylinde'
#WRAP_TYPE = 'moebius'
#WRAP_TYPE = 'torus'


UPDATE_ALGORITHM = 'life regular' # 'life custom'
UPDATE_ALGORITHM = 'life custom'
COUNT_LIST = [1]

FIGSIZE = (7, 7)

PROB = 0.4
IS_RANDOM = True
INITIAL_SETUP = True
INITIAL_SETUP = False

LAYOUT_ID = 1

LAYOUT_DICT = dict()
LAYOUT_DICT[1] = \
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#LAYOUT_INITIALIZATION_DICT = {'rectangular': initialize_rectangular_cells}