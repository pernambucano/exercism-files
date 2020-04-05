class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        for string in matrix_string.split("\n"):
            row = []
            for number in string.split(" "):
                row.append(int(number))
            self.matrix.append(row)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        result = []
        for row in self.matrix:
            result.append(row[index - 1])
        return result

