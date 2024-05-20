import random

class Ship:
    def __init__ (self, size, orientation, start):
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
            else: # 'V'
                    coordinates.append((x + i, y))
    return coordinates

    class Board:
        def __init__ (self, size):
            self.size = size
            self.grid = [['~' for _ in range(size)] for _ in range(size)]
            self.ships = []

        def place_ship(self, ship):
            for (x, y) in ship.coordinates:
                self.grid[x][y] = 'S'
        self.ships.append(ship)
        return True

        def receive_attack(self, position)
         x, y = position
          if self.grid[x][y] == 'S':
            self.grid[x][y] = 'X'
            return "Hit"
        elif self.grid[x][y] == '~':
            self.grid[x][y] = 'O'
            return "Miss"
        return "Already tried"

        