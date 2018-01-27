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

    fig, ax = plt.subplots()    
    ax.matshow(compare, cmap=plt.cm.PuBuGn)
    plt.xticks(np.arange(0, x), input1)
    plt.yticks(np.arange(0, y), input2)
    plt.show()

    
if __name__ == "__main__":
    twod("SPELLSLAUGHTER", "WITHOUTLAUGHTER")
