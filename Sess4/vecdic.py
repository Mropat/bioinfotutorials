import numpy as np
import matplotlib.pyplot as plt


def mergeA_with_average(lab_A, lab_B):
    
    laba_hash = {}
    labb_hash = {}

    lab_a_list = list()
    lab_b_list = list()
    
    laba_handler = open(lab_A, "r")
    labb_handler = open(lab_B, "r")
        
    for line in laba_handler.readlines():
        split_a_line = line.split(" ")
        split_a_key = split_a_line[0]
        split_a_value = split_a_line[1].rstrip()
        laba_hash[split_a_key] = float(split_a_value)

    for line in labb_handler.readlines():
        split_b_line = line.split (", ")
        split_b_key = split_b_line[0]
        split_b_value = split_b_line[1].rstrip()
        labb_hash[split_b_key] = float(split_b_value)       
 

    laba_handler.close()
    labb_handler.close()

    all_keys = list(laba_hash.keys() | labb_hash.keys())
        
    for key in all_keys:
        lab_a_list.append(laba_hash.get(key, 0))
        lab_b_list.append(labb_hash.get(key, 0))


    labaarray = np.array(laba_hash.keys())
    labbarray = np.array(labb_hash.keys())
    


    bins = np.linspace(0,125, num=125)
    plt.hist(laba_hash.values(), bins, alpha = 1, edgecolor = "white", color = "red", label= "Grpup A")
    plt.hist(labb_hash.values(), bins, alpha = 0.5, edgecolor ="white", color = "blue", label = "Group B")
    plt.yticks(range(0, 20, 3))
    plt.xticks(range(0, int(max(laba_hash.values()))+1, 10))
    plt.xlabel("Value range")
    plt.ylabel("Count")
    plt.legend(loc='upper right')
    plt.show()

    

    

    
    

    

if __name__ == '__main__':
    mergeA_with_average("results_labA.dat", "results_labB.dat")
