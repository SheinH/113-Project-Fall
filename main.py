import os

import matplotlib.pyplot as plt
import numpy as np

from letter_classsifier_machine import LetterClassifierMachine


def average_hit_missed(m, n, data, runs):
    hit_miss_percent = []

    for i in range(runs):
        match, miss = train_and_run(m, n, data)
        hit_miss_percent.append(match / (match + miss))
    print('Mean Accuracy after {} runs: {:.3f}%\n'.format(runs, np.mean(hit_miss_percent) * 100))
    return hit_miss_percent


def train_and_run(m, n, data):
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

    machine_classifier.reset()

    return match, miss


def get_pos_int(prompt):
    answer = ''
    while answer == '':
        try:
            answer = int(input(prompt))
            if answer > 12 or answer < 1:
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


# def edit_n_value(current):
#     print('\nCurrent n value set to: {}'.format(current))
#     val = get_pos_int('Enter new value for n in range 1 - 12\n')
#
#     return val
#
#
# def edit_m_value(current):
#     print('\nCurrent m value set to: {}'.format(current))
#     val = get_pos_int('Enter new value for m in range 1 - 12\n')
#     return val


def get_input(string, validator):
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
    hist_bool = True
    data = preload_data()
    n = 3
    m = 4
    runs = 1000
    def modify_n_m():
        n = int(get_input('n (1 - 12) = ', lambda x: int(x) in range(1, 13)))
        m = int(get_input('m = ', lambda x: int(x) > 0))
        return n, m

    choice = get_input('Modify n and m? (y/n): ', lambda x: x.lower() == 'y' or x.lower() == 'n').lower()
    if choice == 'y':
        n, m = modify_n_m()
    while choice.lower() != 'q':
        print('Enter the number corresponding to the choice below to select or q to exit')
        print('1. Change values of n and m')
        print('2. Change run behavior (Default is 10K runs w/ histogram display)')
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
    def opencsv(filename):
        return np.genfromtxt(os.path.join('Data', filename), dtype='U1', delimiter=',')

    h_training = opencsv('H Training.txt')
    l_training = opencsv('L Training.txt')
    test = opencsv('Test Data.txt')
    return h_training, l_training, test


def edit_behavior(runs, hist_bool):
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
