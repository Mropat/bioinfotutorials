def write_complement(input_file_name, output_file_name):
    fh = open(input_file_name, "r")
    outfh = open(output_file_name, "w")
    lines = fh.readlines()
    for x in range (len(lines)):
        test = lines[x]
        test = test.rstrip()
        if ">" in test:
            test = test + " complement" 
            outfh.write(test + '\n')
        else:
            complement = []
            for x in range (len(test)):
                if test[x] == "A":
                    complement.append("T")                                     
                elif test[x] == "T":
                    complement.append("A")
                elif test[x] == "C":
                    complement.append("G")
                elif test[x] == "G":  
                    complement.append("C")
                else:
                    complement.append(test[x])
            scom = ''.join(complement)
            outfh.write(scom + '\n')
    fh.close()
    outfh.close()

if __name__ == "__main__":
    write_complement("dna_sequences", "dna_sequences_comp")
