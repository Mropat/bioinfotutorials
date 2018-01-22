def unique_aa(filename)
    aa_list =[]
    with open(filename, "r") as fh:
        for x , 1 in enumerate(fh):
            line_id = fh.readline[x]
            if ">" in line_id[0]:
                continue
            else:
                for x, 1 in enumerate(line_id)           
                    if line_id[x] in aa_list:
                        continue
                    else:
                        aa_list = aa_list.append(typeline_id[x])

            
                
                

           
        
        
    

unique_aa("uniref90.fasta")
