class Matrix:
    
    def __init__(self, matrix_string):
        self.matrix = [ self.cast_to_int(row.split(' ')) for row in  matrix_string.splitlines()]
        self.shape = (len(self.matrix), len(self.matrix[0])) # shape of matrix
        self.t_matrix = list( zip(*self.matrix) )

    def cast_to_int(self, str_list):
        return list(map(lambda x: int(x), str_list))

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [self.matrix[i][index-1] for i in range(self.shape[0] ) ] 
        # return list(self.t_matrix[index-1])



 

# Great for imperative coding style and comments.

#     Python constructor init doesn't need return statement. Please consider using list comprehension

# Line 6 to 26 can be rewritten
# self.data = [ self.cast_to_int(row.split(' ')) for row in  matrix_string.splitlines()]

# splitlines() will take care of \n

#    def cast_to_int(self, str_list):
#        return list(map(lambda x: int(x), str_list))


# The column: I would suggest to store the transposed matrix in this class as well.

# Create a self.t_matrix so, no iteration over and over again, for performance wise.

# You may use numpy.transpose,or use the zip alternative:


#     def __init__(self, matrix_string):
#         self.matrix = [ self.cast_to_int(row.split(' ')) for row in  matrix_string.splitlines()]
#         self.t_matrix = list( zip(*self.matrix) )

#    def column(self, index):
#         return list(self.t_matrix[index-1])


       
