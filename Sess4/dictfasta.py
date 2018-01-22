def parse_fasta(filename):
    mydic = {}
    keyline = ""
    with open(filename, "r") as fh:
        for line in fh.readlines():
            if ">" in line[0]:
                keyline = line[1:]
                continue
            else:
                mydic[keyline.rstrip()] = line.rstrip()
    return mydic

if __name__ == "__main__":
    parse_fasta("example.fasta")
