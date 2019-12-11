import numpy as np
import random


class LetterClassifierMachine():
    l_trained = [np.zeros((7,4))]
    choice_sets = []
    def __init__(self):
        tmp_indexes = list(range(0, 11))
        index_list = []
        for v in range(1,13):
            if(v % 3 == 0):
                self.choice_sets.append(index_list)
                index_list = []
            if(len(tmp_indexes) != 0):
                index_list.append(tmp_indexes.pop(random.randint(0, len(tmp_indexes)-1)))

    def train_h_set(self):
        print(self.l_trained)

