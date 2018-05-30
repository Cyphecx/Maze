import random


class Maze:

    def __init__(self, height, width, cell_size=1):
        self.height = height
        self.width = width
        self.cell_size = cell_size
        self.cells = []
        self.init_cells()

    def init_cells(self):
        for i in range(0, self.height):
            row = []
            for k in range(0, self.width):
                row.append(Cell(i, k))
            self.cells.append(row)

    def gen_maze(self):
        visited_locations = [self.cells[random.randint(0, self.height)][random.randint(0, self.width)]]

        def next_cell(cell):
            moves = []
            current_x = cell.get_x()
            current_y = cell.get_y()

            if not visited_locations.__contains__(self.cells[current_x][current_y - 1]):
                moves.append("u")
            if not visited_locations.__contains__(self.cells[current_x][current_y + 1]):
                moves.append("d")
            if not visited_locations.__contains__(self.cells[current_x - 1][current_y]):
                moves.append("l")
            if not visited_locations.__contains__(self.cells[current_x + 1][current_y]):
                moves.append("r")

            random.shuffle(moves)

            if moves[0] == "u":
                return self.cells[current_x][current_y - 1]
            elif moves[0] == "d":
                return self.cells[current_x][current_y + 1]
            elif moves[0] == "l":
                return self.cells[current_x - 1][current_y]
            elif moves[0] == "r":
                return self.cells[current_x + 1][current_y]
            else:
                return None

        def step(cell):
            visited_locations.append(cell)
            next_step = next_cell(cell)
            break_walls(cell, next_step)
            step(next_step)

        def break_walls(cell1, cell2):
            print("foobar")

    def print_maze(self):
        for x in self.cells:
            print(x)


class Cell:

    def __init__(self, x, y):
        self.walls = ["left", "right", "top", "bottom"]
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


maze = Maze(20, 20)
maze.print_maze()
