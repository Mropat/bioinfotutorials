def parse_fasta(filename):
    mydicc = {}
    keyline = ""
    with open(filename, "r") as fh:
        for line in fh.readlines():
            if ">" in line[0]:
                keyline = line[1:]
                continue
            else:
                mydicc[keyline.rstrip()] = line.rstrip()
    return dict(mydicc)

if __name__ == "__main__":
    parse_fasta("example.fasta")
