class Garden(object):

    STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry',
    ]

    PLANTS = {
        'C' : 'Clover',
        'G' : 'Grass',
        'R' : 'Radishes',
        'V' : 'Violets'
    }

    def __init__(self, diagram, students=None):
        self.rows = diagram.splitlines()
        self.students = sorted(students if students else self.STUDENTS)
        self.student_index = {name:index for (index, name) in enumerate(self.students)}

    def plants(self, student):
        row_index = self.student_index[student] * 2
        plant_char = ''.join(row[row_index : row_index + 2] for row in self.rows)
        return [self.PLANTS[plant] for plant in plant_char]
