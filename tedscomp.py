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
        line = line.rstrip()
        if ">" == line[0]:
            line += " complement" 
            outfh.write(test + '\n')
        else:
            new_line = ""
            for char in line:
                if char in complement:
                    char = complement[char]
                new_line += char
                
            outfh.write(new_line + '\n')
