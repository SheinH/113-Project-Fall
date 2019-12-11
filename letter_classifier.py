
import random
import os

from data_generator import HGenerator, LGenerator

class LetterClassifier():
    ''' Class is used to show and classify data '''
    cwd = os.getcwd()
    training_h_file_name = cwd + '/H Training.txt'
    training_l_file_name = cwd + '/L Training.txt'

    def __show_letter(self, letter):
        '''Shows letter as pixels of zeros and ones

        Keyword arguments:
        letter -- array length 12 of 0s and 1s
        '''
        for pos in range(len(letter)):
            print(letter[pos], end = ' ')
            if ((pos + 1) % 3 == 0):
                print()
    
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
            return ','.join([str(letter).strip('[]').replace(' ', ''),classifification.upper()]), classifification.upper()
    
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
        classified_letters = []

        h_set = []
        l_set = []

        while len(h_set) < 300 or len(l_set) < 300:
            if(len(h_set) >= 300):
                letter = l_gen.getNewLetterWithCorrupt()
            elif(len(l_set) >= 300):
                letter = h_gen.getNewLetterWithCorrupt()
            else:
                if(random.randint(1,2) == 1):
                    letter = l_gen.getNewLetterWithCorrupt()
                else:
                    letter = h_gen.getNewLetterWithCorrupt()
            
            c, v = self.__classify(letter)
            if(c != ''):
                if(v == 'H'):
                    h_set.append(c)
                elif(v == 'L'):
                    l_set.append(c)
        self.__write_data_to_files(h_set, l_set)
    
            

