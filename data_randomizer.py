import csv
import random

original = open('data/data.csv', 'r')

data_random = open('data/data_random.csv', 'w')

lines = original.readlines()
original.close()

random.shuffle(lines)

data_random.writelines(lines)
data_random.close()