import math
import re

def tailor_sin(x, epsilon):
    series_sum = 0
    term = x
    n = 1
    if epsilon <= 0:
        print("Epsilon must be positive")
        return None
    while abs(term) > epsilon:
        series_sum += term
        term = - term * x**2 / ((2*n) * (2*n+1))
        n += 1
    return series_sum

def get_min(input_arr):
    arr_min = input_arr[0]
    for i in range(len(input_arr)):
        if input_arr[i] < arr_min:
            arr_min = input_arr[i]
    return arr_min

def edit_text(input_text):
    if "-" in input_text:
        input_text = input_text.replace("-", "--")
    if "+" in input_text:
        input_text = input_text.replace("+", "++")
    pattern = r"\d+"
    match = re.search(pattern, input_text)
    if match:
        input_text = input_text.replace(match.group(), "")
    return input_text

while True:
    task = int(input("Input task: "))
    if task == 1:
        print("Exact sin(pi/6):", math.sin(math.pi/6))
        print("Tailor sin(pi/6):", tailor_sin(math.pi/6, 0.00001))
        print("\n")
    elif task == 2:
        arr = list(map(int, input("Input array:").split()))
        print("Array minimum:", get_min(arr))
        print("\n")
    elif task == 3:
        text = input("Input text: ")
        print("New text:", edit_text(text))
        print("\n")
    else:
        print("Error: Invalid task number")
