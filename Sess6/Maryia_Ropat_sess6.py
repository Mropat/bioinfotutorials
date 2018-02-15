import numpy as np


def longest_substring(input1, input2):
    if input1 == input2:
        print([input1])
        return [input1]
    results = []
    x = len(input1)
    y = len(input2)
    maxcount = 0
    currcount = 0
    store_matrix = np.zeros((y+1, x+1), dtype=np.int64)
    for yscan in range(1, y+1):
        for xscan in range(1, x+1):
            if input1[xscan-1] == input2[yscan-1]:
                store_matrix[yscan][xscan] = store_matrix[yscan-1][xscan-1] + 1
                currcount = store_matrix[yscan][xscan]
                if currcount > maxcount:
                    results = [input2[yscan-currcount : yscan]]
                    maxcount = currcount
                elif currcount == maxcount:
                  results.append(input2[yscan-currcount : yscan])
    print(results)
    return results
                                 
if __name__ == '__main__':
    # Include your five test cases here:
    assert longest_substring('DEABCDEEFXQERT', 'DEFQBDEEFAQERT') == ['DEEF', 'QERT']
    assert longest_substring("SPELLSLAUGHTER","LAUGHTER") == ["LAUGHTER"]
    assert longest_substring("ABGTRARA","ABGATTAAAA") == ["ABG"]
    assert longest_substring("WORDS","WORDS") == ["WORDS"]
    assert longest_substring("RAINMAN","MAN") == ["MAN"]
    assert longest_substring("MAMAM","AMA") == ["AMA"]
    assert longest_substring("ABC","DEF") == []
