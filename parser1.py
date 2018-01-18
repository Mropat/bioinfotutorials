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
