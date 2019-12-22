import random


class HGenerator:
    '''Letter generator class with a stronger probability of being classified
        as letter H
    '''
    __CAPITAL_BASES = [
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
    ]

    def getNewLetterWithCorrupt(self):
        '''Generate a new letter with base H and less than 4 corrupted pixels '''
        base = list(self.__CAPITAL_BASES[random.randint(0, 2)])
        for value in range(random.randint(0, 2)):
            pos = random.randint(0, 11)
            base[pos] = self.__corrupt_pixel(base[pos])

        return base

    def __corrupt_pixel(self, pixel):
        '''Corrupt pixel flips from 0 to 1 or 1 to 0

        Keyword Arguments:
        pixel -- Either a 0 or 1 integer to be flipped
        '''
        if pixel == 1:
            return 0
        return 1


class LGenerator:
    '''Letter generator class with a stronger probability of being classified
    as letter L
    '''
    __CAPITAL_BASES = [
        [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
    ]

    def getNewLetterWithCorrupt(self):
        '''Generate a new letter with base H and less than 4 corrupted pixels '''

        base = list(self.__CAPITAL_BASES[random.randint(
            0, len(self.__CAPITAL_BASES) - 1)])
        for value in range(random.randint(0, 3)):
            pos = random.randint(0, 11)
            base[pos] = self.__corrupt_pixel(base[pos])

        return base

    def __corrupt_pixel(self, pixel):
        '''Corrupt pixel flips from 0 to 1 or 1 to 0

        Keyword Arguments:
        pixel -- Either a 0 or 1 integer to be flipped
        '''
        if pixel == 1:
            return 0
        return 1
