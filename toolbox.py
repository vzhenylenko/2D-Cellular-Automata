# Tools->Pdf+video
# Add standard neighbour type to triangle and hex
# Add self correlations for cell to stat functions
# TODO: create separate file for experiments: Experiments.py
from lattices import *
import matplotlib.pyplot as plt


class Experiment1:
    def run_experiment(self):
        init_frac = 0.9
        steps = 20
        n = 100
        m = 100
        configs_list = generate_configs_list(['rectangular'],
                                             ['tor'],
                                             ['none'],
                                             ['regular'],
                                             ['regular'])
        for config in configs_list:
            ca = CellularAutomata(n, m, config[0], config[1], config[2], config[3], config[4], 'random', init_frac)
            densities = []
            densities.append(init_frac)
            for i in range(steps - 1):
                ca.next()
                # collect stats
                densities.append(ca.lattice.get_stat_density())
            # todo: make aggregated stats
            plt.plot(densities)
            plt.savefig('densities.png')
            print(densities)
        # save aggregated stats

        # todo: generate_report()

        print('Experiment ran succesfully')


# Done
def generate_configs_list(lattice_types,
                          surface_types,
                          boundary_types,
                          # boundary_sequences,
                          rule_types,
                          neig_types):
    configs_list = []
    for l in lattice_types:
        for s in surface_types:
            for b in boundary_types:
                for r in rule_types:
                    for n in neig_types:
                        configs_list.append((l, s, b, r, n))
    return configs_list


# TODO
def generate_report(images):
    '''
	Create report_builder
	'''


# TODO
def generate_video(ca, steps):
    '''
	Img_list = []
	For i in range(steps):
	ca.to_image() <--- add class CA_to_image (no) X
	Img add iteration number
	Img_list.append
	Img

	Img_list
	'''
    pass


if __name__ == '__main__':
    ex = Experiment1()
    ex.run_experiment()
