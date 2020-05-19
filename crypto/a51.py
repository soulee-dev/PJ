import random

x = []
y = []
z = []
outlist = []

checkingbit = 0

def rand():
    for i in range(19):
        x.append(random.randrange(0,2))

    for i in range(22):
        y.append(random.randrange(0,2))
    
    for i in range(23):
        z.append(random.randrange(0,2))
        
rand()

print(x, z)

for i in range(64):
    q = x[8]
    w = y[10]
    e = z[10]

    if ((q+w+e) >= 2):
        checkingbit = 1
    else:
        checkingbit = 0

    out = 0

    if(checkingbit == 1):
        if(q == 1 and w == 1 and e == 1):
            out = (q ^ w) ^ e
        elif(q == 1 and w == 1):
            out = q ^ w
        elif(q == 1 and e == 1):
            out = q ^ e
        elif(w == 1 and e == 1):
            out = w ^ e
    else:
        if(q == 0 and w == 0 and e == 0):
            out = (q ^ w) ^ e
        elif(q == 0 and w == 0):
            out = q ^ w
        elif(q == 0 and e == 0):
            out = q ^ e
        elif(w == 0 and e == 0):
            out = w ^ e

    outlist.append(out)

    a = (((x[18] ^ x[17]) ^ x[16]) ^ x[13])
    b = (y[21] ^y[20])
    c = (((z[22] ^ z[21]) ^ z[20]) ^ z[7])

    x.pop()
    y.pop()
    z.pop()

    x.insert(0, a)
    y.insert(0, b)
    z.insert(0, c)
    
print(outlist)

#ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ 수고하세여 ^^ 
