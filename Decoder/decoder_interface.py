from abc import abstractmethod


class AbstractDecoder:
    algorithms = []

    @abstractmethod
    def digest(self):
        pass

    @abstractmethod
    def hexdigest(self):
        pass

    @abstractmethod
    def update(self, data):
        pass

    def __init__(self, algorithm=None):
        self.__algorithm = algorithm

    @property
    def algorithm(self):
        return self.__algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        if algorithm in self.algorithms:
            self.algorithm = algorithm

