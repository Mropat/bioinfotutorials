def unique_aa(filename):
    aa_list =[]
    with open(filename, "r") as fh:
        for line in fh.readlines():
            if ">" in line[0]:
                continue
            else:
                for char in line:
                    if char.isalpha():
                        if char not in aa_list:
                            aa_list.append(char)
    popin_line = "aa_list =" + "{}\n".format(aa_list)
    with open ("aafasta2.py", "r+") as selfedit:
        insert_c = selfedit.readlines()
        insert_c[1] = popin_line
        selfedit.seek(0)
        selfedit.writelines(insert_c)
if __name__ == "__main__":
    unique_aa("example.fasta")
