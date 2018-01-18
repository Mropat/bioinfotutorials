def is_protein(seq):
    aatrue = "ACDEFGHIKLMNPQRSTVWY"
    if all (x in aatrue for x in seq):
        return True
    else:
        return False
is_protein("NHUHAUH")

def longest_line(file_name):
    suchlong = 0
    fh = open("test_longest_line.dat", "r")
    lines = fh.readlines()
    lc = len(lines)
    for x in range (0,lc):
        count = len(lines[x])
        if count >= suchlong:
            suchlong = count
    fh.close()
    return (suchlong)
longest_line("test_longest_line.dat")


def parse_fasta(file_name):
    fh = open(file_name, "r")
    lines = fh.readlines()
    joneslist = []
    for x in range (len(lines)):
        test = lines[x]
        if ">" in test:
            continue
        else:
            test.rstrip()	
            joneslist.append(test)
    fh.close()
    return joneslist

if __name__ == "__main__":
    parse_fasta("T0834.jhE3.ur50.fasta")

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
            test = test.replace("A","1")
            test = test.replace("T","2")
            test = test.replace("C","3")
            test = test.replace("G","4")
            
            test = test.replace("1","T")
            test = test.replace("2","A")
            test = test.replace("3","G")
            test = test.replace("4","C")
            outfh.write(test + '\n')
    fh.close()
    outfh.close()

if __name__ == "__main__":
    write_complement("dna_sequences", "dna_sequences_comp")
