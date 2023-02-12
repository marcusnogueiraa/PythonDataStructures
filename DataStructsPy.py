import numpy as np


class Vector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self._values = np.empty(self.capacity, dtype=int)

    def log(self):
        if self.last_position == -1:
            print('Empty Vector')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self._values[i])

    def insert(self, value):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
        else:
            self.last_position += 1
            self._values[self.last_position] = value

    def search_index(self, value):
        for i in range(self.last_position + 1):
            if value == self._values[i]:
                return i
        return None

    def delete_index(self, index):
        if index == None:
            return None
        else:
            for i in range(index, self.last_position):
                self._values[i] = self._values[i+1]

            self.last_position -= 1

    def delete_value(self, value):
        index = self.search_index(value)
        return self.delete_index(index)

