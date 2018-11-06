import itertools

from decoder_interface import AbstractDecoder
from base import Base
from solver import solver


class Permutation(AbstractDecoder):
    algorithms = ["permutation"]

    def __init__(self, alphabet=None, algorithm=None):
        super(Permutation, self).__init__(algorithm)
        self.__alphabet = alphabet
        self.result = None

    @property
    def alphabet(self):
        return self.__alphabet

    @alphabet.setter
    def algorithm(self, alphabet):
        self.alphabet = alphabet

    def update(self, data):
        if self.alphabet is None:
            key_maps = set()
            map(lambda x: key_maps.add(x), data)
        else:
            key_maps = set(self.alphabet)

        key_dict = itertools.permutations(key_maps)
        self.result = dict()
        for i in key_dict:
            new_data = data
            for l in range(0, len(i)):
                new_data = new_data.replace(i[l], str(l))
            new_data = int(new_data, len(key_maps))
            self.result.update({i: new_data})

    def digest(self):
        value = solver(self.result)
        self.alphabet = value[1]
        return value[0]

    def hexdigest(self):
        value = solver(self.result)
        self.alphabet = value[1]
        return value[0].hex()
