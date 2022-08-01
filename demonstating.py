from percolation_problem import Percolation

if __name__ == '__main__':
    n = int(input('Enter the size of a lattice:\n'))
    open_number = int(input('Enter the number of cells you want to open:\n'))
    grid = Percolation(n)
    for i in range(open_number):
        grid.open_random_cell()
    if grid.percolates():
        print('The lattice percolates')
    else:
        print('The lattice does not percolate')

    grid.print()
