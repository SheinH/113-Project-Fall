import matplotlib.pyplot as plt
import numpy as np
import math

from letter_classifier_manual import LetterClassifierManual
from letter_classsifier_machine import LetterClassifierMachine

import os


def average_hit_missed(m,n,runs):
    hit_miss_percent = []

    for i in range(runs):

        match, miss = train_and_run(m, n)
        hit_miss_percent.append(match / (match + miss))
    print('Mean Accuracy after {} runs: {:.3f}%\n'.format(runs,np.mean(hit_miss_percent) * 100))
    return hit_miss_percent


def train_and_run(m, n):
    machine_classifier = LetterClassifierMachine(m, n)
    machine_classifier.setup(m,n)

    machine_classifier.train_l_set()
    machine_classifier.train_h_set()
    cwd = os.getcwd()

    f = open(cwd + '/Data/Test Data.txt', 'r')
    match, miss = 0, 0
    for line in f:
        if(line.strip() != ''):
            classification = line.strip().split(',')[-1]
            letter = line.strip().split(',')[:-1]
            c = machine_classifier.classify(letter)
            if (c == classification):
                match += 1
            else:
                miss += 1

    machine_classifier.reset()
    f.close()

    return match, miss

def get_pos_int(prompt):
    answer = ''
    while answer == '':
        try:
            answer = int(input(prompt))
            if(answer > 12 or answer < 1):
                print('Error, choice must be in range 1 - 12.')
                answer = ''
        except ValueError as e:
            print('Error, choice must be in range 1 - 12.')
    return answer

def create_histogram(data, runs):
    fig = plt.figure(figsize=(10, 10))

    plt.hist(data, bins=100, histtype='step')
    plt.xlabel('Accuracy Percentage')
    plt.ylabel('Occurrences')
    plt.title('Histogram of {} Runs for Letter Classifier'.format(runs))
    plt.show()

def edit_n_value(current):
    print('\nCurrent n value set to: {}'.format(current))
    val = get_pos_int('Enter new value for n in range 1 - 12\n')

    return val

def edit_m_value(current):
    print('\nCurrent m value set to: {}'.format(current))
    val = get_pos_int('Enter new value for m in range 1 - 12\n')
    return val

def main_options():
    # TODO: Edit n and m behavior as N should be tuple size and M is number of tuples where
    # 1<=M<INFINITY M touples are randomly assigned addresses
    choice = ''
    n = 3
    m = 12 // n
    runs = 1000
    hist_bool = True

    while choice.lower() != 'q':
        print('Enter the number corresponding to the choice below to select or q to exit')
        print('1. Change n value (Changes m depending on entered n)')
        print('2. Change m value (Changes n depending on entered m)')
        print('3. Change run behavior (Default is 10K runs w/ histogram display)')
        print('4. Run')
        choice = input()
        if(choice != ''):
            val = choice[0]
            if(val.lower() == 'q'):
                pass
            elif(val == '1'):
                n = edit_n_value(n)
                print('n set to be {}\n'.format(n))
                m = math.ceil(12 / n)
            elif(val == '2'):
                m = edit_m_value(m)
                print('m set to be {}\n'.format(m))
                n = math.ceil(12 / m)
            elif(val == '3'):
                runs, hist_bool = edit_behavior(runs, hist_bool)
            elif(val == '4'):
                print('\nRunning....')
                if(hist_bool):
                    create_histogram(average_hit_missed(m, n, runs), runs)
                else:
                    average_hit_missed(m, n, runs)
            else:
                print('Invalid Input\n\n')
                choice = ''

def edit_behavior(runs, hist_bool):
    choice = ''
    while choice.lower() != 'q':
        print('\nEnter the number corresponding to the choice below to select or q to exit')
        print('1. Turn "Show Histogram" on or off. Current: {}'.format(hist_bool))
        print('2. Edit the Number of Runs before the average is printed. Current: {}'.format(runs))
        choice = input()
        if(choice != ''):
            val = choice[0]
            if(val.lower() == 'q'):
                pass
            if(val == '1'):
                hist_bool = not hist_bool
            if(val == '2'):
                runs = get_runs_prompt(runs)
    return runs, hist_bool


def get_runs_prompt(runs):
    val = ''
    while val == '':
        print('\nEnter the number of runs that you would like to run before the mean value is shown.')
        try:
            val = int(input())
            if(val < 1):
                print('Invalid Input. Runs must be greater than 1.')
                val = ''
        except:
            print('Invalid Input')
            val = ''
    return val

def cli_menu():
    print('CLI Menu for Final Project - Fall 2019 Letter Classifier')
    print('Authors: Nick W, Shein H, Ekaterina A, Raul M\n\n')
    main_options()

def main():
    cli_menu()


main()
