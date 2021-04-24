class InvalidInputException(Exception):
    def __init__(self, x, y, field_width, field_height):
        self.message = ("The cell ({}, {}) cannot fit into the field of size {}x{}"
                        .format(x, y, field_width, field_height))
        super().__init__(self.message)

        
class TooMuchCellsException(Exception):
    def __init__(self, count, max_count):
        self.message = ("Cannot generate {} living cells because the entire field can only contain {} cells"
                        .format(count, max_count))
        super().__init__(self.message)
