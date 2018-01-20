def pi_digs(n):
    x = 0
    pi = 1
    npi = 0
    b = 0.00001
    y = 1 + n*2
    if n % 2 == 1:
        y *= -1
    for loops in range (n):
        x = x + (1/y)
        npi = x * 4
        if abs(pi - npi) > b:
            pi = npi
            print (npi)
pi_digs(600)
