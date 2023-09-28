import numpy as np

for data_path in ("./data/data85.txt", "./data/data70.txt", "./data/data42.txt", "./data/data21.txt", "./data/data10.txt"):
    data = np.array([])
    with open(data_path) as f:
        contents = f.readlines()[1:]
        for row in contents:
            stuff = float(row)
            if stuff > 400000:
                data = np.append(data, stuff)
    print(f"Standard deviation is: {np.std(data)}. Mean is: {np.mean(data)}. Length: {data.size}")

