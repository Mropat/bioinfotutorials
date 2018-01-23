### Parse into dictionary

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


### Collect a list of unique aminoacids

def unique_aa(filename):
    aa_set = set()
    with open(filename, "r") as fh:
        for line in fh:
            if ">" in line[0]:
                continue
            else:
                for char in line:
                    if char not in aa_set:
                        if char.isalpha():
                            aa_set.add(char)
    popin_line = "aa_list = " + "{}\n".format(sorted(list(aa_set)))
    return popin_line
       
            
        
### Merge group results
        
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


### Save unique results

def save_unique(lab_A, lab_B, output_filename):
    laba_hash = {}
    labb_hash = {}
    uniques = {}
    with open(output_filename, "w") as writehandler:
        laba_handler = open(lab_A, "r")
        labb_handler = open(lab_B, "r")
        for line in laba_handler.readlines():
            split_a_line = line.split(" ")
            split_a_key = split_a_line[0]
            split_a_value = split_a_line[1].rstrip()
            laba_hash[split_a_key] = split_a_value

        for line in labb_handler.readlines():
            split_b_line = line.split (", ")
            split_b_key = split_b_line[0]
            split_b_value = split_b_line[1].rstrip()
            labb_hash[split_b_key] = split_b_value

        for key, val in labb_hash.items():
            if key not in laba_hash:
                uniques[key] = val

        for key, val in laba_hash.items():
            if key not in labb_hash:
                uniques[key] = val

        laba_handler.close()
        labb_handler.close()
        
        for key, val in uniques.items():
            printing = key + " "+ str(val) + "\n"
            writehandler.write(printing)


def CRISPR_module(guide, insert):
    with open ("Maryia_ropat_sess4.py", "r+") as selfedit:
        PAM = 0
        insert_c = selfedit.readlines()
        for line in insert_c:
            PAM +=1
            if guide in line:
                break
        insert_c[PAM-1] = insert_c[PAM-1] + "\n"
        insert_c[PAM] = insert + "\n"
        selfedit.seek(0)
        selfedit.writelines(insert_c)
            

        

if __name__ == '__main__':
    save_unique("results_labA.dat", "results_labB.dat", "results_unique.dat")
    merge_with_average("results_labA.dat", "results_labB.dat", "results_merged.dat")
    parse_fasta("example.fasta")
    CRISPR_module("list of unique aminoacids", unique_aa("example.fasta"))
