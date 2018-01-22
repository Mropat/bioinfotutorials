def save_unique(lab_A, lab_B, output_filename):
    laba_hash = {}
    labb_hash = {}
    uniques = {}
    with open(output_filename, "w") as writehandler:
        laba_handler = open(lab_A, "r")
        labb_handler = open(lab_B, "r")
        for line in laba_handler.readlines():
            split_a_line = line.split(" ")
            split_a_key = split_a_line[0]
            split_a_value = split_a_line[1].rstrip()
            laba_hash[split_a_key] = split_a_value

        for line in labb_handler.readlines():
            split_b_line = line.split (", ")
            split_b_key = split_b_line[0]
            split_b_value = split_b_line[1].rstrip()
            labb_hash[split_b_key] = split_b_value

        for key, val in labb_hash.items():
            if key not in laba_hash:
                uniques[key] = val

        for key, val in laba_hash.items():
            if key not in labb_hash:
                uniques[key] = val

        laba_handler.close()
        labb_handler.close()
        
        for key, val in uniques.items():
            printing = key + " "+ str(val) + "\n"
            writehandler.write(printing)      

if __name__ == '__main__':
    save_unique("results_labA.dat", "results_labB.dat", "unique.dat")
