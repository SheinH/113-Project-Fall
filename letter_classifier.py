
import random
import os

from data_generator import HGenerator, LGenerator


class LetterClassifier():
    ''' Class is used to show and classify data '''
    cwd = os.getcwd()
    training_h_file_name = cwd + '/Data/H Training.txt'
    training_l_file_name = cwd + '/Data/L Training.txt'

    def __classify(self, letter):
        ''' Classify the letter shown as either H or L and return choice as CSV.

        Keyword arguments:
        letter -- array length 12 of 0s and 1s
        '''
        self.__show_letter(letter)
        classifification = input("L or H (Enter to skip): ")
        print()
        if(classifification == ''):
            return '', ''
        else:
            return ','.join([str(letter).strip('[]').replace(' ', ''), classifification.upper()]), classifification.upper()

    def __count_file_lines(self, filename):
        ''' Count the lines of a file if it exists

        Keyword arguments:
        filename -- string representation of where file is located on the OS
        '''
        count = 0
        try:
            f = open(filename, 'r')
        except:
            return 0

        for l in f:
            count += 1

        return count

    def __show_letter(self, letter):
        '''Shows letter as pixels of zeros and ones

        Keyword arguments:
        letter -- array length 12 of 0s and 1s
        '''
        for pos in range(len(letter)):
            print(letter[pos], end=' ')
            if ((pos + 1) % 3 == 0):
                print()

    def __write_data_to_files(self, h_set, l_set):
        ''' Append training data to respective files.

        Keyword arguments:
        h_set -- list of csv strings in the format LETTER,H
        l_set -- list of csv strings in the format LETTER,L
        '''
        f = open(self.training_h_file_name, 'a+')
        f.write('\n'.join(h_set))
        f.close()

        f = open(self.training_l_file_name, 'a+')
        f.write('\n'.join(l_set))
        f.close()

    def classifyLetters(self):
        ''' Classify a minimium of 300 numbers for the L set and H set.'''
        h_gen = HGenerator()
        l_gen = LGenerator()
        h_done = self.__count_file_lines(self.training_h_file_name)
        l_done = self.__count_file_lines(self.training_l_file_name)

        classified_letters = []
        h_set = []
        l_set = []
        iteration = 0

        while l_done < 300 or h_done < 300:
            print('{} out of {} Ls completed'.format(l_done, 300))
            print('{} out of {} Hs completed'.format(h_done, 300))

            if(l_done >= 300):
                letter = l_gen.getNewLetterWithCorrupt()
            elif(h_done >= 300):
                letter = h_gen.getNewLetterWithCorrupt()
            else:
                if(random.randint(1, 2) == 1):
                    letter = l_gen.getNewLetterWithCorrupt()
                else:
                    letter = h_gen.getNewLetterWithCorrupt()

            c, v = self.__classify(letter)
            if(c != ''):
                if(v == 'H'):
                    h_set.append(c)
                    h_done += 1
                    iteration += 1
                elif(v == 'L'):
                    l_set.append(c)
                    l_done += 1
                    iteration += 1

            # Save after 20 new data points as do not want to lose data on crash or boredom
            if(iteration >= 20):
                iteration = 0
                self.__write_data_to_files(h_set, l_set)
                h_set = []
                l_set = []

        self.__write_data_to_files(h_set, l_set)
