import random

def cx_uniform(s,t):
    pattern = [random.randint(0,1) for x in range(len(s))]
    u = [a if b==1 else c for a,b,c in zip(s,pattern,t)]
    v = [a if b==0 else c for a,b,c in zip(s,pattern,t)]
    return u,v

def mut_randP(s, val):
    h = len(s)-1
    l = len(s[0])-1
    for x in range(val):
        r = [random.randint(0,h), random.randint(0,l)]
        diff = random.randint(-2,2)
        s[r[0]][r[1]] = str(int(s[r[0]][r[1]]) + diff)
    return s
