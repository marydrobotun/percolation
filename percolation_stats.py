from percolation_problem import Percolation
from statistics import mean, stdev


class PercolationStats:
    def __init__(self, n, number_of_experiments):
        self.probabilities = None
        self.n = n
        self.experiments = number_of_experiments

    def make_the_experiment(self):
        self.probabilities = []
        for i in range(self.experiments):
            grid = Percolation(self.n)
            while not grid.percolates():
                grid.open_random_cell()
            # print(grid.get_number_of_open_cells())
            self.probabilities.append(grid.get_number_of_open_cells()/(self.n*self.n))

    def get_avg(self):
        if self.probabilities:
            avg = (mean(self.probabilities))
            return avg
        else:
            raise Exception('Please run the make_experiment() before calculating')

    def get_std(self):
        if self.probabilities:
            avg = (stdev(self.probabilities))
            return avg
        else:
            raise Exception('Please run the make_experiment() before calculating')




