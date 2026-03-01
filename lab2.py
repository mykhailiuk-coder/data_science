import numpy as np

while True:
    task = int(input("Input task: "))
    if task == 1: 
        ks = np.arange(0, 100)
        terms = 1 / (np.log(ks + 20) + np.exp(ks))
        total = np.sum(terms)
        print(total)
    if task == 2:
        m = int(input("Input number of rows: "))
        n = int(input("Input number of columns: "))
        input_data = input("Input matrix: ")
        matrix = np.fromstring(input_data, sep=' ').reshape(m, n)
        row_means = np.mean(matrix, axis=1)
        print("Your matrix\n", matrix)
        print("Average from every row:", row_means)
    else:
        print("Error: Invalid task number")
