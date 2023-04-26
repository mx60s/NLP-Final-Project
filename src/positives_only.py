f1 = open('data/tagged_data/trag.txt', 'r')

f2 = open('data/data-positives-only/relis_valid.x', 'w')

ex_pairs = f1.readlines()
pos_exs = []

print(len(ex_pairs))

for i in range(len(ex_pairs) - 1):
    if ex_pairs[i + 1] == "1\n":
        pos_exs.append(ex_pairs[i])

f2.writelines(pos_exs)

f1.close()
f2.close()

print(f'{len(pos_exs)} positive samples collected out of {len(ex_pairs) / 2} samples')
