from abc import ABCMeta, abstractmethod
import random

class Lattice(metaclass=ABCMeta):

    def __init__(self, size):
        pass

    @abstractmethod
    def update(self):
        pass

    def get_stat_density(self):
        return sum(self.cells) / len(self.cells) # TODO: change - if array

    @abstractmethod
    def get_boundary_density(self):
        pass


class OneDimLattice(Lattice):
    
    def __init__(self, n, center_layout=None, init_prob=0.3):
        self.cells = [0] * n  # TODO: change to numpy array
        self.n = n

    # TODO: different types of initiaization of 0 and 1s


    def initialize_cells(self, init_type, init_prob):
        if init_type == 'random':
            self.cells = [1 if random.uniform(0, 1) <= init_prob else 0 for i in range(self.m * self.n)]
        elif init_type == 'center':
            pass
        elif init_type == 'center_random':
            pass
        else:
            raise ValueError('Enter correct argument for intitial conditions')
        return [0, 0, 0, 1]


    def get_boundary_density(self):
        count = 0
        for i in range(n - 1):
            if self.cells[i] != self.cells[i + 1]:
                count += 1
        return count


class TwoDimLattice(Lattice):
    # m horizontal dimension, n vertical dimension
    # starts from right bottom place

    # Done
    def __init__(self, m, n,
             surface_type='tor',
             boundary_type='regular',
             rule_type='regular',
             neigh_type='regular',
             init_type='random',
             init_prob=0.3,
             center_size=None,
             center_layout=None,
             upd_prob=0.5):

        self.m = m
        self.n = n
        self.cells = [0] * n * m
        self.surface_type = surface_type
        self.boundary_type = boundary_type
        self.rule_type = rule_type
        self.neigh_type = neigh_type
        self.upd_prob = upd_prob
        self.initialize_cells(init_type, init_prob, center_size, center_layout)
        self.initialize_neigh_matrix(n, m, surface_type, neigh_type)

        # random - Done
        # center - todo index enumeration


    def initialize_cells(self, init_type, init_prob, center_size, center_layout=None):
        if init_type == 'random':
            self.cells = [1 if random.uniform(0, 1) <= init_prob else 0 for i in range(self.m * self.n)]
        elif init_type == 'center':
            m_start = 0 # todo
            n_start = 0 # todo
            center_indices = []  # todo
            for local_ind, global_ind in enumerate(center_indices):
                self.cells[global_ind] = center_indices[local_ind] # todo double check this line
        elif init_type == 'center_random':
            center_indices = []
            for global_ind in center_indices:
                self.cells[global_ind] = 1 if random.uniform(0, 1) <= init_prob else 0
        else:
            print(init_type)
            raise ValueError('Enter correct argument for intitial conditions')


    # Done
    def get_surface_boundary(self):
        boundary_indices = []
        n = self.n
        m = self.m

        if self.surface_type in ['cylinder', 'moebius_band']:
            boundary_indices = boundary_indices + list(range(m))
            boundary_indices = boundary_indices + [i + (n - 1) * m for i in range(m)]

        elif self.surface_type == 'rectangular':
            boundary_indices = boundary_indices + list(range(m))
            boundary_indices = boundary_indices + [i + (n - 1) * m for i in range(m)]
            boundary_indices = boundary_indices + [n * i for i in range(1, m - 1)]
            boundary_indices = boundary_indices + [n * i - 1 for i in range(2, m)]

        return boundary_indices

    # Done
    def update_cells(self):
        for i, cell in enumerate(self.cells):
            neighs = [self.cells[j] for j in self.neigh_matrix[i]]
            if self.rule_type == 'regular':
                self.cells[i] = self.update_rule_regular(cell, neighs)

        boundary_indices = self.get_surface_boundary()

        if self.boundary_type == 'random':
            for ind in boundary_indices:
                self.cells[ind] = 1 if random.uniform(0, 1) <= self.upd_prob else 0

        if self.boundary_type == 'oscillating':
            for ind in boundary_indices:
                self.cells[ind] = self.boundary_sequence[self.sequence_ind]
            self.sequence_ind = (self.sequence_ind + 1) % len(self.boundary_sequence)

    # TODO: add more update rules (later)

    def update_rule_regular(self, cell, neighs):
        val = 1 if (cell + sum(neighs)) >= (len(neighs) + 1) / 2 else 0
        return val


    def index_to_tuple(self, ind):
        return (ind % self.m, ind / self.m)


    def tuple_to_index(self, tup):
        return tup[0] * self.m + tup[1]


    def initialize_neigh_matrix(self, n, m, surface_type):
        pass


    def get_boundary_density(self):
        pass


    def get_spatial_correlations(self):
        pass


# Done tor
# todo other
class RectangularLattice(TwoDimLattice):
    
    def initialize_neigh_matrix(self, n, m, surface_type, neigh_type='regular'):
        self.neigh_type = neigh_type

        self.neigh_matrix = []
        for i_n in range(n):
            for i_m in range(m):
                neighs = []
                neighs.append(self.tuple_to_index(((i_m - 1) % m, i_n)))
                neighs.append(self.tuple_to_index(((i_m + 1) % m, i_n)))
                neighs.append(self.tuple_to_index((i_m, (i_n - 1) % n)))
                neighs.append(self.tuple_to_index((i_m, (i_n + 1) % n)))

                if self.neigh_type == '8':
                    neighs.append(self.tuple_to_index(((i_m - 1) % m, (i_n - 1) % n)))
                    neighs.append(self.tuple_to_index(((i_m + 1) % m, (i_n - 1) % n)))
                    neighs.append(self.tuple_to_index(((i_m - 1) % m, (i_n + 1) % n)))
                    neighs.append(self.tuple_to_index(((i_m + 1) % m, (i_n + 1) % n)))

                self.neigh_matrix.append(neighs)

            # todo: add all other possibilities
        if surface_type == 'klein_bottle':
            pass


# tor - done
# other - todo
class TriangularLattice(TwoDimLattice):
    
    def initialize_neigh_matrix(self, n, m, boundary_type, neigh_type='regular'):
        self.neigh_matrix = []
        for i_n in range(n):
            for i_m in range(m):
                neighs = []
                neighs.append(self.tuple_to_index(((i_m - 1) % m, i_n)))
                neighs.append(self.tuple_to_index(((i_m + 1) % m, i_n)))
                neighs.append(self.tuple_to_index((i_m, (i_n - 1) % n)))
                neighs.append(self.tuple_to_index((i_m, (i_n + 1) % n)))

                if i_n % 2 == 0:
                    neighs.append(self.tuple_to_index(((i_m + 1) % m, (i_n - 1) % n)))
                    neighs.append(self.tuple_to_index(((i_m + 1) % m, (i_n + 1) % n)))
                else:
                    neighs.append(self.tuple_to_index(((i_m - 1) % m, (i_n - 1) % n)))
                    neighs.append(self.tuple_to_index(((i_m - 1) % m, (i_n + 1) % n)))

                self.neigh_matrix.append[neighs]

            # tor is by default

        if boundary_type == 'klein_bottle':
            # reverse in horizontal direction top & bottom rows
            for i_m in range(m):
                self.neigh_matrix[i_m].remove(self.tuple_to_index((i_m, n - 1)))
                if i_n % 2 == 0:
                    self.neigh_matrix[i_m].remove(self.tuple_to_index(((i_m + 1) % m, n - 1)))
                else:
                    self.neigh_matrix[i_m].remove(self.tuple_to_index(((i_m - 1) % m, n - 1)))

                self.neigh_matrix[i_m].remove(self.tuple_to_index((i_m, n - 1)))
                self.neigh_matrix[i_m + m * (n - 1)]

        elif boundary_type == 'cylinder':
            # remove top & bottom rows
            pass
        elif boundary_type == 'moebius_band':
            # remove top & bottom , reverse upward right and left
            pass
        elif boundary_type == 'rectangular':
            # remove up $ down and left & right
            pass


# tor - done
# other - todo
class HexagonalLattice(TwoDimLattice):
    
    def initialize_neigh_matrix(self, n, m, boundary_type, neigh_type='regular'):
        self.neigh_matrix = []
        for i_n in range(n):
            for i_m in range(m):
                neighs = []
                if i_n % 4 in [0, 3]:
                    neighs.append(self.tuple_to_index(((i_m - 1) % m, i_n)))
                    neighs.append(self.tuple_to_index(((i_m + 1) % m, i_n)))
                    if i_n % 4 == 0:
                        neighs.append(self.tuple_to_index((i_m, (i_n - 1) % n)))
                    else:
                        neighs.append(self.tuple_to_index((i_m, (i_n + 1) % n)))

                else:
                    neighs.append(self.tuple_to_index((i_m, (i_n - 1) % n)))
                    neighs.append(self.tuple_to_index((i_m, (i_n + 1) % n)))
                    if i_n % 4 == 1:
                        neighs.append(self.tuple_to_index(((i_m - 1) % m, (i_n + 1) % n)))
                    else:
                        neighs.append(self.tuple_to_index(((i_m + 1) % m, (i_n + 1) % n)))

                self.neigh_matrix.append[neighs]

        if boundary_type == 'cylinder':
            pass
        # remove top & bottom rows
        elif boundary_type == 'moebius_band':
            pass
        # remove top & bottom , reverse upward right and left
        elif boundary_type == 'rectangular':
            pass

        # remove up $ down and left & right  # TODO


class CellularAutomata:

    def __init__(self, n, m, lattice_type, surface_type, boundary_type, rule_type, neigh_type, init_type, init_prob):
        # check argument and create appropriate Lattice instance
        if lattice_type == 'rectangular':
            self.lattice = RectangularLattice(m, n, surface_type, boundary_type, rule_type, neigh_type, init_type, init_prob)
        # elif lattice_type == 'triangular':

    def next(self):
        self.lattice.update_cells()

    def make_iterations(self, steps):  # for loop (steps) later yield
        pass

# Todo
class RandomCellularAutomata(CellularAutomata):
    
    def update(self):
        # Calc sum + rand.uniform/gauss <-- add as parameter
        pass
