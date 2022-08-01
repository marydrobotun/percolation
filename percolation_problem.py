import UF
from random import randint
from PIL import Image, ImageColor
from PIL import ImageDraw


class Percolation:
    def __init__(self, n, probability_of_percolation=0.1):
        self.n = n
        self.grid = []
        self.probability = probability_of_percolation
        self.UF = UF.UF(n * n)
        for i in range(n * n):
            self.grid.append(0)

    def get_number_of_open_cells(self):
        number=0
        for i in self.grid:
            if i==1:
                number+=1
        return number

    def open(self, row, col):
        self.grid[row * self.n + col] = 1
        might_be_neighbours = [[row - 1, col], [row, col - 1], [row + 1, col], [row, col + 1]]
        neighbours = []
        for curr in might_be_neighbours:
            if 0 <= curr[0] < self.n and 0 <= curr[1] < self.n:
                neighbours.append(curr[0] * self.n + curr[1])
        for neighbour in neighbours:
            if self.grid[neighbour] == 1:
                self.UF.union(row * self.n + col, neighbour)

    def open_random_cell(self):
        p = randint(0, self.n - 1)
        q = randint(0, self.n - 1)
        #print(p, q)
        self.open(p, q)

    def connected_to_up(self, row, col):
        for i in range(self.n):
            if self.UF.find(row * self.n + col, i) and self.grid[i] == 1:
                return True

        return False


    def print(self):
        image = Image.new("RGB", (1000, 1000))

        draw = ImageDraw.Draw(image)
        for i in range(self.n):
            for j in range(self.n):
                if (self.grid[j * self.n + i]) == 1:
                    if self.connected_to_up(j, i):
                        draw.rectangle((i * 50, j * 50, i * 50 + 50, j * 50 + 50), fill=ImageColor.getrgb("blue"),
                                       outline=ImageColor.getrgb("blue"))
                    else:
                        draw.rectangle((i * 50, j * 50, i * 50 + 50, j * 50 + 50), fill=ImageColor.getrgb("white"),
                                       outline=ImageColor.getrgb("blue"))
                else:
                    draw.rectangle((i * 50, j * 50, i * 50 + 50, j * 50 + 50), fill=ImageColor.getrgb("black"),
                                   outline=ImageColor.getrgb("blue"))
        image.show()

    def percolates(self):
        upper_sites = []
        down_sites = []
        for i in range(self.n):
            upper_sites.append(i)
            down_sites.append(self.n * (self.n - 1) + i)
        for down_site in down_sites:
            for upper_site in upper_sites:
                if self.UF.find(upper_site, down_site):
                    return True
        return False


if __name__ == "__main__":

    test = Percolation(10)
    for i in range(100):
        test.open_random_cell()

    print(test.percolates())
    test.print()
