def compute_gc(sequence):
    allcount = len(sequence)
    gccount = sequence.count("GC", 0, -1)
    print (gccount*2/allcount)
    
    

def dist(a, b):
    counta = a.count("", 0, -1)
    countb = b.count("", 0, -1)
    distance = 0
    if counta != countb:
        print ("sequence lengths don't match")
    for x in range (0, counta):
        if a[x] != b[x]:
            distance = distance + 1
        x = x + 1
    print(distance)
    
    

    
def score(a, b):
    if a == b:
        print("1")
    else: 
        print ("0")
        
        
    
def matchStrings(stringA, stringB):
    if  len(stringA) > len(stringB):
        matchl = len(stringB)
    else:
        matchl = len(stringA)
    match = 0
    for z in range (0, matchl):
        if stringA[z] == stringB[z]:
            match = match +1
        z = z + 1
    print (match)
    
if __name__=="__main__":
    inseq = input("Insert sequence to determine GC content")
    compute_gc(inseq)
    
    distseq = input (" To calculate distance, input fist fequence")
    distseq2 = input ("Input second sequence")
    dist(distseq, distseq2)
    
    sca = input ("Input a single character")
    scb = input ("Input second character")
    score(sca, scb)
    
    ms1 = input ("Input first string to count matches")
    ms2 = input ("Input second string")
    matchStrings(ms1, ms2)
     
                
    
