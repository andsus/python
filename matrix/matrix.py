class Matrix:
    
    def __init__(self, matrix_string):
        self.matrix = [self.cast_to_int(row.split()) for row in  matrix_string.splitlines()]

    def cast_to_int(self, str_list):
        return [int(v) for v in str_list]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [m[index-1] for m in self.matrix] 


