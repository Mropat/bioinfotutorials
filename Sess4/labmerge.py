def merge_with_average(lab_A, lab_B, output_filename):
    result_hash = {}
    labb_hash = {}
    with open(output_filename, "w") as writehandler:
        laba_handler = open(lab_A, "r")
        labb_handler = open(lab_B, "r")
        for line in laba_handler.readlines():
            split_a_line = line.split(" ")
            split_a_key = split_a_line[0]
            split_a_value = split_a_line[1].rstrip()
            result_hash[split_a_key] = split_a_value

        for line in labb_handler.readlines():
            split_b_line = line.split (", ")
            split_b_key = split_b_line[0]
            split_b_value = split_b_line[1].rstrip()
            labb_hash[split_b_key] = split_b_value

        for key, val in labb_hash.items():
            if key in result_hash:
                Bval = float(labb_hash.get(key))
                Aval = float(result_hash.get(key))
                avg = round(sum([Bval, Aval])/2, 2)
                result_hash[key] = avg
            else:
                result_hash[key] = val

        laba_handler.close()
        labb_handler.close()
        
        for key, val in result_hash.items():
            printing = key + " "+ str(val) + "\n"
            writehandler.write(printing)      

if __name__ == '__main__':
    merge_with_average("results_labA.dat", "results_labB.dat", "results_merged.dat")
