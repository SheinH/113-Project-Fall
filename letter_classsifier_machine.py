import numpy as np
import os
import random
import itertools

class LetterClassifierMachine():
    __l_trained = np.zeros((4, 8))
    __h_trained = np.zeros((4, 8))
    choice_sets = []

    def __init__(self, m, n, data):
        # TODO: HANDLE LOGIC OF m && n here w/ array sizes
        choice_sets = []
        self.__l_trained = np.zeros((m, 2 ** n))
        self.__h_trained = np.zeros((m, 2 ** n))
        self.data = data
        indices = list(range(0, 12))
        tuples = list(itertools.combinations(indices,n))
        self.choice_sets = np.array(random.sample(tuples,m))

        # tmp_indexes = list(range(0, 12))

        # tmp_indexes = list(range(0, 12))
        # index_list = []
        # for v in range(1, 13):
        #     if(len(tmp_indexes) != 0):
        #         index_list.append(tmp_indexes.pop(
        #             random.randint(0, len(tmp_indexes)-1)))
        #     if(v % n == 0):
        #         self.choice_sets.append(index_list)
        #         index_list = []

    def setup(self, m, n):
        pass
        # #todo change here
        # self.choice_sets = []
        # self.__l_trained = np.zeros((m, 2**n))
        # self.__h_trained = np.zeros((m, 2**n))
        tmp_indexes = list(range(0, 12))
        index_list = []
        # for v in range(1, 13):
        #     if(len(tmp_indexes) != 0):
        #         index_list.append(tmp_indexes.pop(
        #             random.randint(0, len(tmp_indexes)-1)))
        #     if(v % n == 0):
        #         self.choice_sets.append(index_list)
        #         index_list = []

        # for i in range(m):
        #     self.choice_sets.append([random.randint(1, 12)] for i in range(n))
        #     if (len(tmp_indexes) != 0):
        #         index_list.append(tmp_indexes.pop(
        #         random.randint(0, len(tmp_indexes)-1)))
        #     if(i % n == 0):
        #         self.choice_sets.append(index_list)
        #         index_list = []
        # for _ in range(m):
        #     for i in range(n):
        #         self.choice_sets.append([random.randint(1, 12)])
        # index_list = []


    def reset(self):
        self.__l_trained = np.zeros((4, 8))
        self.__h_trained = np.zeros((4, 8))
        self.choice_sets = []

    def train_l_set(self):
        if self.data:
            ld = self.data[1]
            for row in ld:
                for index, tuple in enumerate(self.choice_sets):
                    self.__l_trained[index][self.__get_position(tuple,row)] += 1

        # cwd = os.getcwd()
        # f = open(cwd + '/Data/L Training.txt', 'r')
        # for line in f:
        #     if (line.strip() != ''):
        #         letter = line.strip().split(',')[:-1]
        #         for index, tuple in enumerate(self.choice_sets):
        #             self.__l_trained[index][self.__get_position([
        #                 letter[pos] for pos in tuple
        #             ])] += 1
        # f.close()

    def train_h_set(self):

        if self.data:
            data = self.data[0]
            for row in data:
                index = 0
                for tuple in self.choice_sets:
                    self.__h_trained[index][self.__get_position(tuple, row)] += 1
                    index += 1
        # cwd = os.getcwd()
        # f = open(cwd + '/Data/H Training.txt', 'r')
        # for line in f:
        #     if (line.strip() != ''):
        #         letter = line.strip().split(',')[:-1]
        #     for index, tuple in enumerate(self.choice_sets):
        #         self.__h_trained[index][self.__get_position([
        #             letter[pos] for pos in tuple
        #         ])] += 1
        # f.close()

    def print_l_set(self):
        print(self.__l_trained)

    def print_h_set(self):
        print(self.__h_trained)


    def __get_position(self, tuple, data):
        vals = data[tuple]
        pos = 0
        i = 0
        for x in vals:
            if x == '1':
                pos = 1 << i | pos
            i += 1
        return pos
        # # TODO: Possible need to change this logic to dictionary as m && n can change
        # total = 0
        # for v in range(len(positions) - 1, 0, -1):
        #     if (positions[v] == '1'):
        #         total += 2 ** int(v)
        # return total

    def classify(self, letter):
        # total_h = 0
        # for index, tuple in enumerate(self.choice_sets):
        #     total_h += self.__h_trained[index][self.__get_position([
        #         letter[pos] for pos in tuple]
        #     )]
        # total_l = 0
        # for index,tuple in enumerate(self.choice_sets):
        #     total_l += self.__l_trained[index][self.__get_position([
        #         letter[pos] for pos in tuple]
        #     )]
        total_h = 0
        total_l = 0
        data = self.data[2]
        index = 0
        for tuple in self.choice_sets:
            total_h += self.__h_trained[index][self.__get_position(tuple, letter)]
            total_l += self.__l_trained[index][self.__get_position(tuple, letter)]
            index += 1

        if (total_h > total_l):
            return 'H'
        elif (total_h < total_l):
            return 'L'
        else:
            return None
