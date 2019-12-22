import os

import matplotlib.pyplot as plt
import numpy as np

from letter_classsifier_machine import LetterClassifierMachine


def average_hit_missed(m, n, data, runs):
    """Calculates the percentages of correct identifications by checking the match arrays
    and dividing them by the overall count """
    hit_miss_percent = []

    for i in range(runs):
        match, miss = train_and_run(m, n, data)
        hit_miss_percent.append(match / (match + miss))
    print('Mean Accuracy after {} runs: {:.3f}%\n'.format(runs, np.mean(hit_miss_percent) * 100))
    return hit_miss_percent


def train_and_run(m, n, data):
    """ calls functions from the letter classifier machine to create the training arrays and update with the
        training data then test what was learned on a test data set.
    """
    machine_classifier = LetterClassifierMachine(m, n, data)
    machine_classifier.train_l_set()
    machine_classifier.train_h_set()

    match, miss = 0, 0

    for letter in data[2]:
        c = machine_classifier.classify(letter[:-1])
        if c == letter[-1]:
            match += 1
        else:
            miss += 1
    return match, miss


def create_histogram(data, runs):
    """ Creates a histogram of the runs to show distribution of the hit% ratios """
    fig = plt.figure(figsize=(10, 10))

    plt.hist(data, bins=100, histtype='step')
    plt.xlabel('Accuracy Percentage')
    plt.ylabel('Occurrences')
    plt.title('Histogram of {} Runs for Letter Classifier'.format(runs))
    plt.show()


def get_input(string, validator):
    """Gets user input and runs it through a validator lambda
    If the input is invalid, the user will be prompted for further input.
    """
    inp = input(string)
    valid = False
    while not valid:
        try:
            valid = validator(inp)
        except:
            pass
        if valid:
            break
        print('Invalid Input\n\n')
        inp = input(string)
    return inp


def main_options():
    """Main event loop for this program"""
    hist_bool = True
    data = preload_data()
    choice = ''
    n = 3
    m = 4
    runs = 1000

    def modify_n_m():
        n = int(get_input('n (1 - 12) = ', lambda x: int(x) in range(1, 13)))
        m = int(get_input('m = ', lambda x: int(x) > 0))
        return n, m

    while choice.lower() != 'q':
        print(f'\nn = {n}, m = {m}\n')
        print('Enter the number corresponding to the choice below to select or q to exit')
        print('1. Change values of n and m')
        print('2. Change run behavior (Default is 1K runs w/ histogram display)')
        print('3. Run')
        choice = get_input('Choice: ', lambda x: x == 'q' or int(x) in range(1, 4))
        if choice != '':
            val = choice[0]
            if val.lower() == 'q':
                pass
            elif val == '1':
                n, m = modify_n_m()
            elif val == '2':
                runs, hist_bool = edit_behavior(runs, hist_bool)
            elif val == '3':
                print('\nRunning....')
                if hist_bool:
                    create_histogram(average_hit_missed(m, n, data, runs), runs)
                else:
                    average_hit_missed(m, n, data, runs)
            else:
                print('Invalid Input\n\n')
                choice = ''


def preload_data():
    """
    Returns 3 item tuple of numpy string arrays
    1st item - Data from H training
    2nd item - Data from L training
    3rd item - Test data
    """

    def open_csv(filename):
        return np.genfromtxt(os.path.join('Data', filename), dtype='U1', delimiter=',')

    h_training = open_csv('H Training.txt')
    l_training = open_csv('L Training.txt')
    test = open_csv('Test Data.txt')
    return h_training, l_training, test


def edit_behavior(runs, hist_bool):
    """allows the user to change if the histogram is printed at the end of the run or to change the number of runs
        the stating values is to print histogram and 1000 runs
    """
    choice = ''
    while choice.lower() != 'q':
        print('\nEnter the number corresponding to the choice below to select or q to exit')
        print('1. Turn "Show Histogram" on or off. Current: {}'.format(hist_bool))
        print('2. Edit the Number of Runs before the average is printed. Current: {}'.format(runs))
        choice = input()
        if choice != '':
            val = choice[0]
            if val.lower() == 'q':
                pass
            if val == '1':
                hist_bool = not hist_bool
            if val == '2':
                runs = get_runs_prompt(runs)
    return runs, hist_bool


def get_runs_prompt(runs):
    """Function for modifying # of runs"""
    val = ''
    while val == '':
        print('\nEnter the number of runs that you would like to run before the mean value is shown.')
        try:
            val = int(input())
            if val < 1:
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
