import numpy as np
#import matplotlib as mpl
#import matplotlib.pyplot as plt

def twod(input1, input2):
    x = len(input1)
    y = len(input2)

    in1 = np.char.array(list(input1))
    mtx1 = np.tile((in1, y), 1) 
    print (mtx1)
    in2 = np.char.array(list(input2)
    mtx2 = np.tile((in2, x), 1)
    #mtx2 = np.rot90(mtx2, 3)
    print (mtx2)



    #compare = np.ones((x, y))
    #compare = compare* (mtx1 == mtx2)
    

    #print (compare)


if __name__ == "__main__":
    twod("ANALOG", "LAMBDA")
