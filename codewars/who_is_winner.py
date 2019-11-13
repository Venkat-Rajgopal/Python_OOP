import numpy as np

pieces_position_list = ["A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "G_Red",
                          "B_Yellow"]


splits = ([i.split('_')[1] for i in pieces_position_list])
_, n_count = np.unique(splits, return_counts=True)
max_val = n_count[0]
val_unique = list(set(splits))

r_count = 0
y_count = 0

while r_count<= max_val or y_count <= max_val:
    for i in splits:
        if val_unique[0] == i:
            r_count += 1
        if val_unique[1] == i:
            y_count += 1
    print(y_count)
