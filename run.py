import random

class Ship:
    def __init__(self, size, orientation, start):
        self.size = size
        self.orientation = orientation
        self.start = start
        self.coordinates = self.generate_coordinates()

    def generate_coordinates(self):
        coordinates = []
        x, y = self.start
        for i in range(self.size):
            if self.orientation == 'H':
                coordinates.append((x, y + i))
            else:  # 'V'
                coordinates.append((x + i, y))
        return coordinates

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['~' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, ship):
        for (x, y) in ship.coordinates:
            if x < 0 or x >= self.size or y < 0 or y >= self.size or self.grid[x][y] != '~':
                return False
        for (x, y) in ship.coordinates:
            self.grid[x][y] = 'S'
        self.ships.append(ship)
        return True

    def receive_attack(self, position):
        x, y = position
        if self.grid[x][y] == 'S':
            self.grid[x][y] = 'X'
            return "Hit"
        elif self.grid[x][y] == '~':
            self.grid[x][y] = 'O'
            return "Miss"
        else:
            return "Already tried"

    def all_ships_sunk(self):
        for ship in self.ships:
            if any(self.grid[x][y] == 'S' for (x, y) in ship.coordinates):
                return False
        return True

    def display(self, reveal_ships=False):
        for row in self.grid:
            print(' '.join(row))
        print()

class MainGame:
    def __init__(self, size):
        self.size = size
        self.player_board = Board(size)
        self.computer_board = Board(size)   

    def setup_board(self, board):
        for size in [5,4,3,3,2]:   
            placed = False
            while not placed:
                orientation = random.choice(['H', 'V'])
                if orientation == 'H':
                    start = (random.randint(0, board.size - 1), random.randint(0, board.size - size))
                else:
                    start = (random.randint(0, board.size - size), random.randint(0, board.size - 1))
                    ship = Ship(size, orientation, start)
                    placed = board.place_ship(ship)

    def play(self):
        self.setup_board(self.player_board)
        self.setup_board(self.computer_board)

                        