import re
import sys

input_file = sys.argv[1] # assumes .txt

with open(input_file, 'r') as f:
    lines = f.readlines()

both = []
pos_only = []
i = 0
while i < len(lines) - 1:
    print(lines[i])
    br1 = re.search(r'<BrainRegion1>(.*)<\/BrainRegion1>', lines[i].strip())
    br2 = re.search(r'<BrainRegion2>(.*)<\/BrainRegion2>', lines[i].strip())

    br1 = br1.groups()[0]
    br2 = br2.groups()[0]

    stripped = re.sub(r'<\/*BrainRegion[1-2]>', '', lines[i])
    
    if lines[i + 1] == "1\n":
        y = 'there is a relation between ' + br1 + ' and ' + br2 + '.\n'
        both.append((stripped, y))
        pos_only.append((stripped, y))
    else:
        y = 'there is no relation between ' + br1 + ' and ' + br2 + '.\n'
        both.append((stripped, y)) 

    i += 2

pos_only_y = open(input_file[:-4] + '_pos.y', "w")
pos_only_x = open(input_file[:-4] + '_pos.x', "w")
for i in range(len(pos_only)):
    pos_only_x.write(pos_only[i][0])
    pos_only_y.write(pos_only[i][1])
pos_only_y.close()
pos_only_x.close()

both_y = open(input_file[:-4] + '.y', "w")
both_x = open(input_file[:-4] + '.x', 'w')
for i in range(len(both)):
    both_x.write(both[i][0])
    both_y.write(both[i][1])
both_y.close()
both_x.close()
