def is_protein(seq):
    aatrue = "ACDEFGHIKLMNPQRSTVWY"
    if all (x in aatrue for x in seq):
        return True
    else:
        return False


def longest_line(file_name):
    suchlong = 0
    fh = open(file_name, "r")
    lines = fh.readlines()
    lc = len(lines)
    for x in range (lc):
        cur = lines[x]
        long = cur.rstrip()     
        if len(long) > suchlong:
            suchlong = len(long)
    fh.close()
    return (suchlong)



def parse_fasta(file_name):
    fh = open(file_name, "r")
    lines = fh.readlines()
    joneslist = []
    for x in range (len(lines)):
        test = lines[x]
        if ">" in test:
            continue
        else:
            test = test.rstrip()	
            joneslist.append(test)
    fh.close()
    return joneslist




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
    parse_fasta("T0834.jhE3.ur50.fasta")
    longest_line("test_longest_line.dat")
    is_protein("NHUHAUH")
    




#Alternative complement without hashmaps:
    
"""def write_complement2(input_file_name, output_file_name):
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
    write_complement2("dna_sequences", "dna_sequences_comp")"""
