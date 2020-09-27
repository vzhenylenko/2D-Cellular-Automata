class Experiment1:

    def generate_configs_list(self,
                              lattice_types,
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

    def run_experiment(self):
        init_frac = 0.9
        steps = 20
        n = 100
        m = 100
        configs_list = self.generate_configs_list(['rectangular'],
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

        print('Experiment ran succesfully')

if __name__ == '__main__':
    ex = Experiment1()
    ex.run_experiment()
