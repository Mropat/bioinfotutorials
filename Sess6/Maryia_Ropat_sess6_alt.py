import numpy as np
import timeit


def longest_substring(input1, input2):

    if input1 == input2:
        return {input1}

    results = set()
    x = len(input1)
    y = len(input2)
    maxcount = 0
    store_matrix = np.zeros((y, x), dtype=np.int64)

    for yscan in range(y):
        if yscan >y-maxcount:
            break
        for xscan in range(x):
            if xscan > x-maxcount:
                break
            if store_matrix[yscan][xscan] > 0:
                continue 
            if input1[xscan] == input2[yscan]:
                store_matrix[yscan][xscan] = 1
                currcount = 1
                while currcount + xscan < x and \
                        currcount + yscan < y and \
                        input1[xscan + currcount] == input2[yscan + currcount]:
                    
                    store_matrix[yscan + currcount][xscan + currcount] = currcount + 1
                    currcount += 1                    
                if currcount > maxcount:
                    maxcount = currcount
                    results = {input2[yscan:yscan+currcount]}
                elif currcount == maxcount:
                    results.add(input2[yscan:yscan+currcount])

    return results
                        

                                 
if __name__ == '__main__':
    assert longest_substring("SPELLSLAUGHTER","LAUGHTER") == {"LAUGHTER"}
    assert longest_substring("ABGTRARA","ABGATTAAAA") == {"ABG"}
    assert longest_substring("WORDS","WORDS") == {"WORDS"}
    assert longest_substring("RAINMAN","MAN") == {"MAN"}
    assert longest_substring("MAMAM","MAM") == {"MAM"}
    assert longest_substring("ABCDEF","DEF") == {"DEF"}
    assert longest_substring('DEABCDEEFXQERT', 'DEFQBDEEFAQERT') == {'DEEF', 'QERT'}
    assert longest_substring("ABC","DEF") == set()
