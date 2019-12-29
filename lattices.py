import random

class Lattice:
	cells
	neigh_matrix
	neigh_type # ????? few neigh types for rectangular, but only one for hexagonal & triangular 
	 # similar mechanism across all lattice types in 2d
	surface_type #tor, klein, moebius, cylinder, square
	boundary_type
	boundary_sequence
	sequence_ind 

	def __init__(self, size):
    	pass 
    def update(self):
    	pass   
    def get_density(self):
    	return self.cells.sum() / length(self.cells)
    def get_boundary_density(self):
    	pass
    	
'''--------------------------------------------------------------------------------------------'''

class OneDimLattice(Lattice):
	n

	def __init__(self, n, center_layout=None, prob=0.3):
    	self.cells = [0] * n  # TODO change to numpy array
    	self.n = n
    
    # TODO: different types of initiaization of 0 and 1s
    def initialize_cells(self, init_type, prob):
		if init_type == 'random':
			self.cells = [1 if random.uniform(0, 1) <= prob else 0 for i in range(self.m * self.n)]
		elif init_type == 'center':
			pass
		elif init_type == 'center_random':
			pass
		else:
			raise ValueError('Enter correct argument for intitial conditions')
		return [0,0,0,1]

    def get_boundary_density(self):
    	count = 0
    	for i in range(n - 1):
    		if self.cells[i] != self.cells[i + 1]:
    			count += 1
    	return count

'''--------------------------------------------------------------------------------------------'''

class TwoDimLattice(Lattice):
	m, n

    def __init__(self, m, n, boundary_type='tor', init_type='random', prob=0.3, center_size=None, center_layout=None, upd_prob = 0.5):
    	self.m = m
    	self.n = n
    	self.cells = [0] * n * m
    	self.boundary_type = boundary_type
    	self.upd_prob = upd_prob
    	self.initialize_cells(init_type, prob, center_size, center_layout)
    	self.initialize_neigh_matrix(n, m, boundary_type)

    #TODO: actually implement center initialization
    def initialize_cells(self, init_type, prob, center_size, center_layout):
		if init_type == 'random':
			self.cells = [1 if random.uniform(0, 1) <= prob else 0 for i in range(self.m * self.n)]
		elif init_type == 'center':
			center_indices = []
			for local_ind, global_ind in enumerate(center_indices):
				self.cells[global_ind] = center[local_ind]
		elif init_type == 'center_random':
			center_indices = []
			for global_ind in center_indices:
				self.cells[global_ind] = 1 if random.uniform(0, 1) <= prob else 0
		else:
			raise ValueError('Enter correct argument for intitial conditions')

	# TODO: add actual indices
	def get_surface_boundary(self):
		boundary_indices = []
		if self.surface_type in ['cylinder', 'moebius_band']:
			pass
		if self.surface_type == 'square':
			pass
		return boundary_indices

    def update_cells(self):
    	for i, cell in enumerate(self.cells):
    		neighs = [self.cells[j] for j in self.neigh_matrix[i]]
    		self.cells[i] = self.update_rule(cell, neighs)
    	boundary_indices = self.get_surface_boundary()
    	if boundary_type == 'random':
    		for ind in boundary_indices:
    			self.cells[ind] = 1 if random.uniform(0, 1) <= self.upd_prob else 0
    	if boundary_type == 'oscillating':
    		for ind in boundary_indices:
    			self.cells[ind] = self.boundary_sequence[self.sequence_ind]
    		self.sequence_ind = (self.sequence_ind + 1) % len(self.boundary_sequence)

    #TODO: add more update rules (later)
    def update_rule(self, cell, neighs):
		val = 1 if (cell + sum(neighs)) >= (len(neighs) + 1) / 2 else 0 
		return val

    def index_to_tuple(self, ind):
		return (ind % self.m, ind / self.m)

	def tuple_to_index(self, tup):
		return tup[0] * self.m + tup[1]

	def initialize_neigh_matrix(self, n, m, boundary_type):
		pass

	def get_boundary_density(self):
    	pass

    def get_spatial_correlations(self):
    	pass


'tor', 'klein_bottle', ('square', 'cylinder', 'moebius') x ('oscillating', 'random', 'reduced')

class RectangularLattice(TwoDimLattice):
	def initialize_neigh_matrix(self, n, m, boundary_type, neigh_type='4'):
		self.neigh_type = neigh_type
    	self.neigh_matrix = []
    	for i_n in range(n):
    		for i_m in range(m):
    			neighs = []
    			neighs.append(tuple_to_index( ((i_m - 1) % m, i_n) ))
	    		neighs.append(tuple_to_index( ((i_m + 1) % m, i_n) ))
	    		neighs.append(tuple_to_index( (i_m, (i_n - 1) % n) ))
	    		neighs.append(tuple_to_index( (i_m, (i_n + 1) % n) ))

    			if self.neigh_type == '8':
    				neighs.append(tuple_to_index( ((i_m - 1) % m, (i_n - 1) % n) ))
	    			neighs.append(tuple_to_index( ((i_m + 1) % m, (i_n - 1) % n) ))
	    			neighs.append(tuple_to_index( ((i_m - 1) % m, (i_n + 1) % n) ))
	    			neighs.append(tuple_to_index( ((i_m + 1) % m, (i_n + 1) % n) ))

	    		self.neigh_matrix.append[neighs]

class TriangularLattice(TwoDimLattice):
    def initialize_neigh_matrix(self, n, m, boundary_type):
    	self.neigh_matrix = []
    	for i_n in range(n):
    		for i_m in range(m):
    			neighs = []
    			neighs.append(tuple_to_index( ((i_m - 1) % m, i_n) ))
	    		neighs.append(tuple_to_index( ((i_m + 1) % m, i_n) ))
	    		neighs.append(tuple_to_index( (i_m, (i_n - 1) % n) ))
	    		neighs.append(tuple_to_index( (i_m, (i_n + 1) % n) ))

    			if i_n % 2 == 0:
	    			neighs.append(tuple_to_index( ((i_m + 1) % m, (i_n - 1) % n) ))
	    			neighs.append(tuple_to_index( ((i_m + 1) % m, (i_n + 1) % n) ))
	    		else:
	    			neighs.append(tuple_to_index( ((i_m - 1) % m, (i_n - 1) % n) ))
	    			neighs.append(tuple_to_index( ((i_m - 1) % m, (i_n + 1) % n) ))

	    		self.neigh_matrix.append[neighs]

class HexagonalLattice(TwoDimLattice):
    def initialize_neigh_matrix(self, n, m, boundary_type):
    	self.neigh_matrix = []
    	for i_n in range(n):
    		for i_m in range(m):
    			neighs = []
    			if i_n % 4 in [0, 3]:
    				neighs.append(tuple_to_index( ((i_m - 1) % m, i_n) ))
	    			neighs.append(tuple_to_index( ((i_m + 1) % m, i_n) ))
	    			if i_n % 4 == 0:
	    				neighs.append(tuple_to_index( (i_m, (i_n - 1) % n) ))
	    			else:
	    				neighs.append(tuple_to_index( (i_m, (i_n + 1) % n) ))

	    		else:
	    			neighs.append(tuple_to_index( (i_m, (i_n - 1) % n) ))
	    			neighs.append(tuple_to_index( (i_m, (i_n + 1) % n) ))
	    			if i_n % 4 == 1:
		    			neighs.append(tuple_to_index( ((i_m - 1) % m, (i_n + 1) % n) ))
		    		else:
	    				neighs.append(tuple_to_index( ((i_m + 1) % m, (i_n + 1) % n) ))

	    		self.neigh_matrix.append[neighs]