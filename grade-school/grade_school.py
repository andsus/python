from bisect import insort 
class School:
    def __init__(self):
        self._db = []

    def add_student(self, name, grade):
        insort(self._db, (grade, name))

    def roster(self):
        return [ name for grade, name in self._db]

    def grade(self, grade_number):
        return [ name for grade, name in self._db if grade == grade_number]
