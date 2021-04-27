import math
import random
import time
from typing import Dict, Tuple, List


class Cell:
    def __init__(self, x, y, is_alive=False):
        self.x = x
        self.y = y
        self.is_alive = is_alive


class Field:
    # Though it looks a bit redundant,
    # storing cells as a dict is better for performance of finding a cell's neighbors
    # and generating the next state
    living_cells: Dict[Tuple[int, int], Cell] = {}
    
    def __init__(self, living_cells_positions: List[Tuple[int, int]] = []):
        self._create_living_cells(living_cells_positions)
    
    def _should_cell_live(self, cell: Cell) -> bool:
        """
        Checks the state of a field and its neighbors to decide whether the field should die or live in the next tick
        """
        living_neighbours_count = self._count_living_neighbors(cell)
        # Any live cell with two or three live neighbours survives
        if cell.is_alive and living_neighbours_count in [2, 3]:
            return True
        # Any dead cell with three live neighbours becomes a live cell
        if not cell.is_alive and living_neighbours_count == 3:
            return True
        # All other live cells die in the next generation. Similarly, all other dead cells stay dead
        return False
    
    def _count_living_neighbors(self, cell: Cell) -> int:
        """Returns a count of horizontally, vertically and diagonally adjacent living cells"""
        count = 0
        # borders of the area in which we are trying to find neighbors
        # Let's assume y axis directs downside and x axis directs to the left
        
        for x in range(cell.x - 1, cell.x + 2):
            for y in range(cell.y - 1, cell.y + 2):
                if cell.x == x and cell.y == y:
                    continue
                if (x, y) in self.living_cells.keys():
                    count += 1
        
        return count
    
    def _create_living_cells(self, living_cells_positions: List[Tuple[int, int]]) -> None:
        """Generates an initial state of the game"""
        for x, y in living_cells_positions:
            self.living_cells[x, y] = Cell(x, y, True)
            
    def randomize(self, count, deviation: int = 5):
        """Creates a game with a random initial state"""
        cells = []
        for i in range(count):
            cells.append(
                (random.randint(-deviation, deviation - 1),
                 random.randint(-deviation, deviation - 1))
            )
        self._create_living_cells(cells)
        return self
    
    def generate_next_state(self) -> Dict[Tuple[int, int], Cell]:
        """Returns the next state of the game"""
        next_state: Dict[Tuple[int, int], Cell] = {}
        for living_cell in self.living_cells.values():
            for x in range(living_cell.x - 1, living_cell.x + 2):
                for y in range(living_cell.y - 1, living_cell.y + 2):
                    cell = Cell(x, y)
                    if (x, y) in self.living_cells.keys():
                        cell = self.living_cells[x, y]
                    if self._should_cell_live(cell):
                        next_state[x, y] = Cell(x, y, True)
        
        self.living_cells = next_state
        
        return self.living_cells
    
    def get_state(self) -> Dict[Tuple[int, int], Cell]:
        return self.living_cells
    
    def display_cli(self) -> None:
        """Prints the current state in the console"""
        if len(self.living_cells.keys()) == 0:
            print('.')
            return
        min_x, min_y = math.inf, math.inf
        max_x, max_y = -math.inf, -math.inf
        for x, y in self.living_cells.keys():
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        for y in range(min_y, max_y + 1):
            chars = ""
            for x in range(min_x, max_x + 1):
                chars += '*' if (x, y) in self.living_cells.keys() else '.'
            print(chars)
        print()


# a simple test script
if __name__ == '__main__':
    field = Field([
        (7, 0),
        (8, 0),
        (9, 0),
        (7, 5),
        (8, 5),
        (9, 5),
    ])
    field.display_cli()
    time.sleep(1)
    
    while True:
        field.generate_next_state()
        field.display_cli()
        time.sleep(1)
