

class Tuple:
    def __init__(self, *args):
        self._data = args
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
       raise TypeError('not supported')
    def __str__(self):
        return self._data
    def __repr__(self):
        return self._data

t = Tuple(1,2,3,'a')
print(t)
t.data = 10
print(t._data)