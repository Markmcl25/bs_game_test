class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['~' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, ship):
        for (x, y) in ship.coordinates:
            if (x < 0 or x >= self.size or y < 0 or y >= self.size or
                    self.grid[x][y] != '~'):
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
            if reveal_ships:
                print(' '.join(row))
            else:
                print(' '.join(['X' if cell == 'X' else 'O' if cell == 'O' else '~' for cell in row]))
        print()

    def get_available_coordinates(self):
        available = []
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] == '~' or self.grid[x][y] == 'S':
                    available.append((x, y))
        return available

