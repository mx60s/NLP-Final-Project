import os
import sys

# find sentences in white text
# add brain regions back into it
# collect positive samples

# need to name the files train/test/valid
# which are which?

data_dir = sys.argv[1]

def loader(fname):
    x = []
    y = []

    with open(fname, 'r') as fr:
        i = 0
        for line in fr:
            if i % 2 == 0:
                x.append(line)
            else:
                if line == '0':
                    y.append('')
                else:
                    y.append('the relation between BR1 and BR2 exists.')

            i += 1

    return x, y

def dumper(x, y, prefix):
    # pmid needed?

    fw_content = open(prefix + ".x", "w")
    fw_label = open(prefix + ".y", "w")
    
    for xx, yy in zip(x,y):
        print(xx, file=fw_content)
        print(yy, file=fw_label)

    fw_content.close()
    fw_label.close()

def worker(fname, prefix):
    x, y = loader(fname)
    dumper(x, y, prefix)


# right now it expects a json but that will probably be different
for split in ['train', 'valid', 'test']:
    worker(os.path.join(f"{data_dir}", f"{split}.txt"), os.path.join(f"{data_dir}", f"relis_{split}"))