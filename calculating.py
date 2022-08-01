from percolation_stats import PercolationStats

if __name__ == "__main__":
    n = int(input("Enter the size of the lattice:\n"))
    experiments = int(input("Enter the number of experiments you want to run:\n"))
    test = PercolationStats(n, experiments)
    test.make_the_experiment()
    print('Mean:        ', test.get_avg())
    print('Stddev:         ', test.get_std())
