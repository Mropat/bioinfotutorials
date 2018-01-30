import numpy as np
import matplotlib.pyplot as plt


def twod(input1, input2):
    
    x = len(input1)
    y = len(input2)

    in1 = np.char.array(list(input1))
    mtx1 = np.tile(in1,(y, 1))
    
    in2 = np.char.array(list(input2))
    mtx2 = np.tile(in2,(x, 1))
    mtx2 = np.rot90(mtx2, 3)

    compare = np.ones((y, x))
    compare = compare* (mtx1 == mtx2)

    
    plt.matshow(compare, cmap=plt.cm.BuPu_r)
    plt.xticks(np.arange(0, x), input1)
    plt.yticks(np.arange(0, y), input2)
    plt.show(block=False)


def reverse_array(input_array):
    rev = input_array[::-1]
    return rev


def sort_array(input_array):
    srt = np.sort(input_array)
    return srt


if __name__ == "__main__":
    reverse_array(np.array([5, 2, 3, 4,5]))
    sort_array(np.array([6, 7, 3, 4,5]))
    twod("SPELLSLAUGHTER", "WITHOUTLAUGHTER")
