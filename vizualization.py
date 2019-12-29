import lattices

def initalize_coordinates(lattice_type):
	coords = [(0,0)]
	return coords

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
    return p

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
    return p
    
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
    return p
    


def make_plot():

