import numpy as np
import os
import random


class LetterClassifierMachine():
    __l_trained = np.zeros((4, 8))
    __h_trained = np.zeros((4, 8))
    choice_sets = []

    def __init__(self, m, n):
        #TODO: HANDLE LOGIC OF m && n here w/ array sizes
        choice_sets = []
        self.__l_trained = np.zeros((m, 2**n))
        self.__h_trained = np.zeros((m, 2**n))

        tmp_indexes = list(range(0, 12))
        index_list = []
        for v in range(1, 13):
            if(len(tmp_indexes) != 0):
                index_list.append(tmp_indexes.pop(
                    random.randint(0, len(tmp_indexes)-1)))
            if(v % n == 0):
                self.choice_sets.append(index_list)
                index_list = []
        
    
    def setup(self, m, n):
        self.choice_sets = []
        self.__l_trained = np.zeros((m, 2**n))
        self.__h_trained = np.zeros((m, 2**n))
        tmp_indexes = list(range(0, 12))
        index_list = []
        for v in range(1, 13):
            if(len(tmp_indexes) != 0):
                index_list.append(tmp_indexes.pop(
                    random.randint(0, len(tmp_indexes)-1)))
            if(v % n == 0):
                self.choice_sets.append(index_list)
                index_list = []

    def reset(self):
        self.__l_trained = np.zeros((4, 8))
        self.__h_trained = np.zeros((4, 8))
        self.choice_sets = []
    def train_l_set(self):
        cwd = os.getcwd()
        f = open(cwd + '/Data/L Training.txt', 'r')
        for line in f:
            if(line.strip() != ''):
                letter = line.strip().split(',')[:-1]
                for v in range(len(self.choice_sets)):
                    self.__l_trained[v][self.__get_position([
                        letter[pos] for pos in self.choice_sets[v]]
                    )] += 1

        f.close()

    def train_h_set(self):
        cwd = os.getcwd()
        f = open(cwd + '/Data/H Training.txt', 'r')
        for line in f:
            if(line.strip() != ''):
                letter = line.strip().split(',')[:-1]
                for v in range(len(self.choice_sets)):
                    self.__h_trained[v][self.__get_position([
                        letter[pos] for pos in self.choice_sets[v]]
                    )] += 1
        f.close()

    def print_l_set(self):
        print(self.__l_trained)

    def print_h_set(self):
        print(self.__h_trained)

    def __get_position(self, positions):
        #TODO: Possible need to change this logic to dictionary as m && n can change
        total = 0
        for v in range(len(positions) - 1, 0, -1):
            if(positions[v] == '1'):
                total += 2**int(v)
        return total

    def classify(self, letter):
        total_h = 0
        for v in range(len(self.choice_sets)):
            total_h += self.__h_trained[v][self.__get_position([
                letter[pos] for pos in self.choice_sets[v]]
            )]
        total_l = 0
        for v in range(len(self.choice_sets)):
            total_l += self.__l_trained[v][self.__get_position([
                letter[pos] for pos in self.choice_sets[v]]
            )]

        if (total_h > total_l):
            return 'H'
        elif (total_h < total_l):
            return 'L'
        else:
            return None
