def compute_gc(sequence):
    allcount = len(sequence)
    if allcount == 0:
        return 0
    gccount = sequence.count("GC")
    return gccount*2/allcount    
    

def dist(a, b):
    counta = len(a)
    countb = len(b)
    distance = 0
    if counta != countb:
        print ("sequence lengths don't match")
        return
    for x in range (counta):
        if a[x] != b[x]:
            distance = distance + 1
    return distance    

    
def score(a, b):
    if a == b:
        return 1
    else: 
        return 0        
        
    
def matchStrings(stringA, stringB):
    if  len(stringA) > len(stringB):
        matchl = len(stringB)
    else:
        matchl = len(stringA)
    match = 0
    for z in range (matchl):        
        match += score(stringA[z],stringB[z])
    return match
    

if __name__=="__main__":
    inseq = input("Insert sequence to determine GC content: ")
    print(compute_gc(inseq))    
    
    distseq = input("To calculate distance, input fist fequence: ")
    distseq2 = input("Input second sequence: ")
    print(dist(distseq, distseq2))
    
    sca = input("Input a single character: ")
    scb = input("Input second character: ")
    print(score(sca, scb))
    
    ms1 = input("Input first string to count matches: ")
    ms2 = input("Input second string: ")
    print(matchStrings(ms1, ms2))
     
                
    
