def compute_gc(sequence):
    allcount = len(sequence)
    if allcount == 0:
        return 0
    gccount = sequence.count("G") + sequence.count("C")
    return gccount/allcount    
    
