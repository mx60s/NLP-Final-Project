import csv
import random
import re

# read in non-segmented brain regions
regions = []

with open('data/regions.csv', newline='') as region_f:
    csvreader = csv.reader(region_f, delimiter=' ', quotechar='|')
    for row in csvreader:
        regions.append(' '.join(row).replace(',', ' ').strip())

# define relations
# connect_words = ['afferent', 'axon', 'connect', 'efferent', 'innervate',
#                 'input', 'interconnect', 'pathway', 'project', 'originate',
#                 'receive', 'terminate']

trans_phrases = [', additionally, ', ', and ', ', while ']

connect_phrases = ['BR is connected to BR', 'input to BR originated from BR',
                   'there are projections from BR to BR',
                   'BR was found to receive afferents from BR',
                   'BR innervates BR', 'BR has pathways to BR']

connect_3 = ['BR is connected to BR and BR', 'BR and BR is connected to BR',
             'there are projections from BR to BR and BR',
             'there are projections from BR and BR to BR',
             'BR was found to receive afferents from BR and BR',
             'BR and BR were found to receive afferents from BR',
             'BR innervates BR and BR', 'BR and BR innervates BR',
             'BR and BR have pathways to BR', 'BR has pathways to BR and BR']

# write to x and y files for comparison later
x = []
y = []

for i in range(1000):
    # forward = True # indicates which relation is used twice in y, alternates in connect_3 list
    for phrase1 in connect_3:
        for phrase2 in connect_phrases:
            for trans in trans_phrases:
                regs = random.sample(regions, 4)

                xx = phrase1 + trans + phrase2 + '\n'
                yy = 'the relation between BR and BR exists; the relation between BR and BR exists.\n'

                for r in regs:
                    xx = xx.replace('BR', r, 1)
                    yy = yy.replace('BR', r, 1)

                x.append(xx)
                y.append(yy)


with open('data/faux_multi_2_relations.x', 'w') as x_file:
    x_file.writelines(x)

with open('data/faux_multi_2_relations.y', 'w') as y_file:
    y_file.writelines(y)
