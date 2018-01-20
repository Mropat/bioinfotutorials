def write_complement2(input_file_name, output_file_name):
    fh = open(input_file_name, "r")
    outfh = open(output_file_name, "w")
    lines = fh.readlines()
    complement = {
        "A" : "T",
        "T" : "A",
        "C" : "G",
        "G" : "C"
    }
    for line in lines:
        line = line.strip()
        if ">" in line:
            line += " complement" 
            outfh.write(line + '\n')
        else:
            new_line = ""
            for nu in line:
                if nu in complement:
                    nu = complement[nu]
                new_line += nu
                
            outfh.write(new_line + '\n')
