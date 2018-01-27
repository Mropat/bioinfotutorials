"""with open ("/usr/local/lib/python3.5/dist-packages/numpy/__init__.py", "r") as np:
    for line in np:
        print(line)"""


import numpy as np
def reverse_array(input_array):
  rev = input_array[::-1]
  return np.copy(rev)

def sort_array(input_array):
    srt = np.array(sorted(input_array))
    return srt


if __name__ == "__main__":
    reverse_array(np.array([5, 2, 3, 4,5]))
    sort_array(np.array([6, 7, 3, 4,5]))



    
