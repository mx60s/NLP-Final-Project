import re
import sys

input_file = sys.argv[1] # assumes .txt

with open(input_file, 'r') as f:
    lines = f.readlines()

both = []
pos_only = []

for i in range(len(lines) - 1):
    print(lines[i])
    stripped = re.sub(r'<\/*BrainRegion[1-2]>', '', lines[i])
    print(stripped)
    br1 = re.match(r'<BrainRegion1>(.*)<\/BrainRegion1>', lines[i].strip())
    br2 = re.match(r'<BrainRegion2>(.*)<\/BrainRegion2>', lines[i].strip())

    print(br1)
    print(br2)

    stripped = re.sub(r'<\/*BrainRegion[1-2]>', '', lines[i])
    
    if lines[i + 1] == "1\n":
        y = 'there is a relation between ' + br1 + ' and ' + br2 + '.'
        both.append((stripped, y))
        pos_only.append((stripped, y))
    else:
        y = 'there is no relation between ' + br1 + ' and ' + br2 + '.'
        both.append((stripped, y))


pos_only_y = open('pos_' + input_file[:-4] + '.y')
pos_only_x = open('pos_' + input_file[:-4] + '.x')
for i in range(len(pos_only)):
    pos_only_x.write(pos_only[i][0])
    pos_only_y.write(pos_only[i][1])
pos_only_y.close()
pos_only_x.close()

both_y = open(input_file[:-4] + '.y')
both_x = open(input_file[:-4] + '.y')
for i in range(len(both)):
    both_x.write(both[i][0])
    both_y.write(both[i][1])
both_y.close()
both_x.close()
