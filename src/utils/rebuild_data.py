import os
import sys

# find sentences in white text
# add brain regions back into it
# collect positive samples

# need to name the files train/test/valid
# which are which?

data_dir = sys.argv[1]

def loader(fname, fn):
    return None

def dumper(content_list, prefix):
    # pmid needed?

    fw_content = open(prefix + ".x", "w")
    fw_label = open(prefix + ".y", "w")
    
    for ele in content_list:
        print(ele[0], file=fw_content)
        print(ele[1], file=fw_label)

    fw_content.close()
    fw_label.close()

def worker(fname, prefix, fn):
    ret = loader(fname, fn)
    dumper(ret, prefix)


for split in ['train', 'valid', 'test']:
    worker(os.path.join(f"{data_dir}", f"{split}.json"), os.path.join(f"{data_dir}", f"relis_{split}"), build_target_seq_relis)