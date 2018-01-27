import numpy as np
import matplotlib.pyplot as plt


def lab_parser(file, splitter):
    with open(file, "r") as lab_handler:
        lab_dictionary = {}
        lab_handler = open(file, "r")
        for line in lab_handler.readlines():
            split_line = line.split(splitter)
            split_key = split_line[0]
            split_value = split_line[1].strip()
            lab_dictionary[split_key] = float(split_value)

    return lab_dictionary

def mergeA_with_average(lab_A, lab_B):
    
    laba_hash = {}
    labb_hash = {}

    lab_a_common = []
    lab_b_common = []
        
    lab_a_dict = lab_parser(lab_A, " ")
    lab_b_dict = lab_parser(lab_B, ", ") 

    common_keys = lab_a_dict.keys() & lab_b_dict.keys()

    colors = []
    for key in common_keys:
        lab_a_common.append(lab_a_dict.get(key))
        lab_b_common.append(lab_b_dict.get(key))
        colors.append(abs(lab_a_common[-1] - lab_b_common[-1]))
    
    plt.scatter(lab_a_common, lab_b_common, c=colors, cmap=plt.cm.spring)
    plt.plot([0,120], [0, 120], "--", linewidth=3, color="black", label ="Most similar" )
    plt.legend(loc="upper right")
    plt.xlabel("Lab A")
    plt.ylabel("Lab B")
    plt.show()
if __name__ == '__main__':
    mergeA_with_average("results_labA.dat", "results_labB.dat")
        



   

    
