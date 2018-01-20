def write_complement(input_file_name, output_file_name):
    fh = open(input_file_name, "r")
    outfh = open("dna_sequences_comp", "w")
    lines = fh.readlines()
    for x in range (len(lines)):
        test = lines[x]
        if ">" in test:
            test = test.replace("REF", "COMP")
            outfh.write(test)
        else:
            test = test.replace("A", "T") 
            test.replace("C", "G") 
            test.replace("G", "C") 
            test.replace("T", "A")
            outfh.replace(test)
    fh.close()
    outfh.close()

if __name__ == "__main__":
    write_complement("dna_sequences", "dna_sequences_comp")
