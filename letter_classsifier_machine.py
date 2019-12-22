import itertools
import random

import numpy as np


class LetterClassifierMachine:

    def __init__(self, m, n, data):
        """Initializes the LCM, generates choice tuples, and saves data"""
        self.__l_trained = np.zeros((m, 2 ** n))
        self.__h_trained = np.zeros((m, 2 ** n))
        self.data = data
        indices = list(range(0, 12))
        tuples = list(itertools.combinations(indices, n))
        self.choice_sets = np.array(random.sample(tuples, min(m, len(tuples))))

    def train(self, dataset, output):
        """ Generalized method for training h and l
        Takes in dataset: numpy array, which contains the csv data
        Matches it with the choice tuples and stores results in output
        """
        for row in dataset:
            samples = np.take(row, self.choice_sets)
            i = 0
            for s in samples:
                output[i][self.__array_to_binary(s)] += 1
                i += 1

    def train_h_set(self):
        """
        data[0] contains csv data for "H Training.txt" self.__h_trained will contain
        frequency data for each choice tuple
        """
        self.train(self.data[0], self.__h_trained)

    def train_l_set(self):
        """
        data[1] contains csv data for "L Training.txt" self.__l_trained will contain
        frequency data for each choice tuple
        """
        self.train(self.data[1], self.__l_trained)

    def print_l_set(self):
        print(self.__l_trained)

    def print_h_set(self):
        print(self.__h_trained)

    def __array_to_binary(self, arr):
        """ Turns an array such as ['1', '0', '1'] into an int: 5
        Used for finding the frequency data for any sample result.
        """
        n = 0
        for value in arr:
            n <<= 1
            if value == '1':
                n += 1
        return n

    def classify(self, letter):
        """ Classifies a letter based on random samples """
        total_h = 0
        total_l = 0
        samples = np.take(letter, self.choice_sets)
        i = 0
        for item in samples:
            index = self.__array_to_binary(item)
            total_h += self.__h_trained[i][index]
            total_l += self.__l_trained[i][index]
            i += 1
        if total_h > total_l:
            return 'H'
        elif total_h < total_l:
            return 'L'
        else:
            return None
